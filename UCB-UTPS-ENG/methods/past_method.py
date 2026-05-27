# methods/past_method.py
# PAST Method - Improved version with higher effective coverage (UCB strategy support)

import os
import ast
import re
import time
import random
import math
import json
from datetime import datetime
from openai import OpenAI
from common.test_executor import TestExecutor
from common.coverage_analyzer import CoverageAnalyzer


# ========== UCB Statistics Manager ==========
class UCBStats:
    """UCB statistics information manager"""

    def __init__(self):
        self.total_count = 0
        self.path_stats = {}  # {path_idx: {'success': int, 'fail': int, 'reward': float, 'total_tries': int}}

    def reset(self):
        """Reset statistics"""
        self.total_count = 0
        self.path_stats = {}

    def update(self, path_idx: int, success: bool, reward: float = None):
        """Update path statistics"""
        key = str(path_idx)
        if key not in self.path_stats:
            self.path_stats[key] = {'success': 0, 'fail': 0, 'reward': 0, 'total_tries': 0}

        if success:
            self.path_stats[key]['success'] += 1
        else:
            self.path_stats[key]['fail'] += 1

        self.path_stats[key]['total_tries'] += 1
        if reward is not None:
            old_reward = self.path_stats[key]['reward']
            old_tries = self.path_stats[key]['total_tries'] - 1
            if old_tries > 0:
                self.path_stats[key]['reward'] = (old_reward * old_tries + reward) / self.path_stats[key]['total_tries']
            else:
                self.path_stats[key]['reward'] = reward

        self.total_count += 1

    def get_success_rate(self, path_idx: int) -> float:
        """Get success rate for a path"""
        key = str(path_idx)
        stats = self.path_stats.get(key, {'total_tries': 0, 'success': 0})
        total = stats['total_tries']
        if total == 0:
            return 0.5  # Initial optimistic estimate
        return stats['success'] / total

    def get_reward(self, path_idx: int) -> float:
        """Get average reward"""
        key = str(path_idx)
        stats = self.path_stats.get(key, {'reward': 0, 'total_tries': 0})
        if stats['total_tries'] == 0:
            return 0.0
        return stats['reward']

    def get_try_count(self, path_idx: int) -> int:
        """Get number of attempts"""
        key = str(path_idx)
        stats = self.path_stats.get(key, {'total_tries': 0})
        return stats['total_tries']

    def calculate_ucb(self, path_idx: int, c: float = 1.414) -> float:
        """
        Calculate UCB value
        UCB = average_reward + c * sqrt(ln(total_tries) / n_i)
        """
        success_rate = self.get_success_rate(path_idx)
        n_i = self.get_try_count(path_idx)

        if n_i == 0:
            return float('inf')

        exploration_bonus = c * math.sqrt(math.log(self.total_count + 1) / n_i)
        return success_rate + exploration_bonus

    def calculate_ucb_tuned(self, path_idx: int, c: float = 1.414) -> float:
        """UCB-Tuned variant"""
        success_rate = self.get_success_rate(path_idx)
        n_i = self.get_try_count(path_idx)

        if n_i == 0:
            return float('inf')

        variance = success_rate * (1 - success_rate)
        exploration_bonus = math.sqrt((math.log(self.total_count + 1) / n_i) *
                                      min(0.25, variance + math.sqrt(2 * math.log(self.total_count + 1) / n_i)))
        return success_rate + c * exploration_bonus

    def save_stats(self, filename: str):
        """Save statistics"""
        stats_data = {
            'total_count': self.total_count,
            'path_stats': self.path_stats
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(stats_data, f, indent=2)

    def load_stats(self, filename: str):
        """Load statistics"""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.total_count = data.get('total_count', 0)
                self.path_stats = data.get('path_stats', {})
            return True
        return False


class PASTMethod:
    """PAST Method - Improved version (UCB strategy support)"""

    def __init__(self, target_file: str, api_key: str = None, base_url: str = None):
        self.target_file = target_file
        self.source = open(target_file, encoding='utf-8').read()
        self.module_name = os.path.splitext(os.path.basename(target_file))[0]
        self.function_name = self._extract_function_name()
        self.params = self._extract_params()
        self.coverage_analyzer = CoverageAnalyzer(target_file)

        # Extract condition paths
        self.paths = self._extract_paths()

        # Initialize LLM client
        self.api_key = api_key or "sk-f0df09ba45bf458dacd7dbe1367c16db"
        self.base_url = base_url or "https://dashscope.aliyuncs.com/compatible-mode/v1"
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

        # Cache
        self.generated_tests = set()
        self.best_test_code = None
        self.best_effective_cov = 0

        # ========== UCB related attributes ==========
        self.use_ucb = False  # Whether to use UCB strategy, default False to keep original behavior
        self.ucb_mode = 'standard'  # 'standard', 'tuned'
        self.ucb_stats = UCBStats()
        self.ucb_c = 1.414  # Exploration parameter
        self.previous_effective_cov = 0  # For calculating reward

    # ========== UCB Configuration Methods ==========
    def enable_ucb(self, c: float = 1.414, mode: str = 'standard'):
        """Enable UCB strategy"""
        self.use_ucb = True
        self.ucb_c = c
        self.ucb_mode = mode
        self.ucb_stats.reset()
        self.previous_effective_cov = 0
        print(f"  [UCB] Enabled, mode={mode}, exploration parameter c={c}")

    def disable_ucb(self):
        """Disable UCB strategy, restore original PAST behavior"""
        self.use_ucb = False
        print(f"  [UCB] Disabled, restored original PAST strategy")

    def _select_path_ucb(self, covered_conds: list, fail_count: list) -> int:
        """
        UCB path selection strategy
        Select the uncovered path with the highest UCB value
        Returns: selected path index, or None if no available path
        """
        candidates = []

        for idx in range(len(self.paths)):
            # Skip covered ones
            if covered_conds[idx]:
                continue

            # Skip ones with too many failures
            if fail_count[idx] >= 3:
                continue

            # Calculate UCB value
            if self.ucb_mode == 'tuned':
                ucb_value = self.ucb_stats.calculate_ucb_tuned(idx, self.ucb_c)
            else:
                ucb_value = self.ucb_stats.calculate_ucb(idx, self.ucb_c)
            candidates.append((idx, ucb_value))

        if not candidates:
            # If no candidates, try resetting failure counts
            for idx in range(len(self.paths)):
                if not covered_conds[idx]:
                    fail_count[idx] = 0
                    if self.ucb_mode == 'tuned':
                        ucb_value = self.ucb_stats.calculate_ucb_tuned(idx, self.ucb_c)
                    else:
                        ucb_value = self.ucb_stats.calculate_ucb(idx, self.ucb_c)
                    candidates.append((idx, ucb_value))

            # Still no candidates, all conditions are covered
            if not candidates:
                return None

        # Sort by UCB value descending, select the maximum
        candidates.sort(key=lambda x: x[1], reverse=True)
        selected_idx = candidates[0][0]

        print(f"        [UCB] Selected path {selected_idx}, UCB={candidates[0][1]:.4f}, "
              f"attempts={self.ucb_stats.get_try_count(selected_idx)}")

        return selected_idx

    def _select_path_original(self, covered_conds: list, fail_count: list) -> int:
        """
        Original PAST path selection strategy (unchanged)
        Prefer uncovered conditions with failure count < 3
        """
        for idx, covered in enumerate(covered_conds):
            if not covered and fail_count[idx] < 3:
                return idx
        return None

    def _extract_function_name(self) -> str:
        try:
            tree = ast.parse(self.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    return node.name
            return os.path.splitext(os.path.basename(self.target_file))[0]
        except:
            return "target_function"

    def _extract_params(self) -> list:
        """Extract function parameters"""
        try:
            tree = ast.parse(self.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == self.function_name:
                    return [arg.arg for arg in node.args.args]
        except:
            pass
        return []

    def _extract_paths(self) -> list:
        """Extract condition paths"""
        try:
            tree = ast.parse(self.source)
        except:
            return []

        paths = []

        class PathVisitor(ast.NodeVisitor):
            def visit_If(self, node):
                cond = ast.unparse(node.test)
                cond = re.sub(r'\s+', ' ', cond.strip())
                paths.append({"condition": cond, "covered": False, "priority": len(cond)})
                paths.append({"condition": f"not ({cond})", "covered": False, "priority": len(cond)})
                self.generic_visit(node)

        PathVisitor().visit(tree)

        # Deduplicate
        unique_paths = []
        seen = set()
        for p in paths:
            cond = p["condition"]
            if cond not in seen:
                seen.add(cond)
                unique_paths.append(p)

        unique_paths.sort(key=lambda x: (-x["priority"], x["condition"]))

        print(f"  [INFO] Extracted {len(unique_paths)} condition paths")
        print(f"  [INFO] Function parameters: {self.params}")
        return unique_paths

    def _generate_param_examples(self) -> str:
        """Generate parameter examples"""
        if not self.params:
            return "No parameters"

        examples = []
        for param in self.params:
            if 'text' in param or 's' in param or 'string' in param:
                examples.append(f'{param}="  hello\\n    world"')
            elif 'value' in param or 'num' in param:
                examples.append(f'{param}=42')
            elif 'flag' in param or 'is_' in param:
                examples.append(f'{param}=True')
            else:
                examples.append(f'{param}="test"')

        return ", ".join(examples)

    def _generate_test_for_path(self, path: dict, max_retries: int = 2,
                                rep_idx: int = 0, iter_idx: int = 0, path_idx: int = 0) -> str:
        """Generate high-quality test for a specific condition path"""

        params_example = self._generate_param_examples()

        prompt = f"""You are a white-box testing expert. Generate a pytest test that can execute the core logic of the target code.

## Target Code (code to test)
File: {self.module_name}.py
```python
{self.source}
```

## Target Function
- Function name: {self.function_name}
- Parameters: {self.params}
- Parameter examples: {params_example}

## Target Condition Path
Condition to cover: {path['condition']}

## Important Rules (must follow)

1. **Must import the original function**, do not redefine it:
   ```python
   from {self.module_name} import {self.function_name}
   ```

2. **Do NOT** redefine the target function inside the test function

3. The test must execute the **core logic** of the function, not just return a value

4. Use @pytest.mark.parametrize to provide multiple test cases

## ⚠️ Test Depth Requirements (very important)

1. **Not only test return values, but also test internal state changes**
2. **For conditional branches, each branch should have corresponding test cases**
3. **For loops, test empty collections, single elements, and multiple elements**
4. **For boundary conditions, test minimum, maximum, and critical values**
5. **For exceptional cases, test invalid inputs and error handling**

## Correct Example
```python
import pytest
from {self.module_name} import {self.function_name}

# Example: Testing identifier validation function
@pytest.mark.parametrize("name,expected", [
    # Valid identifiers
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    # Invalid identifiers (starting with wrong char)
    ("123invalid", False),
    ("1var", False),
    # Reserved words
    ("class", False),
    ("return", False),
    ("if", False),
    # Edge cases
    ("", False),
    ("a", True),
    ("x" * 100, True),  # Long string
])
def test_target_path(name, expected):
    result = {self.function_name}(name)
    assert result == expected
```

Please output only Python code, no other explanation:
"""

        for attempt in range(max_retries):
            try:
                print(f"        [API] Calling API to generate test (attempt {attempt + 1}/{max_retries})...")
                resp = self.client.chat.completions.create(
                    model="qwen-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3,
                    timeout=60
                )

                content = resp.choices[0].message.content
                code = self._extract_code(content)

                if not code:
                    print(f"        [WARN] Failed to extract code")
                    continue

                # Check for incorrect redefinition
                if f'def {self.function_name}' in code and 'from ' not in code:
                    print(f"        [WARN] Detected function redefinition, rejecting")
                    continue

                code = self._fix_code(code)

                # Save generated test code
                os.makedirs("generated_tests", exist_ok=True)
                test_file = f"generated_tests/PAST_{self.module_name}_rep{rep_idx}_iter{iter_idx}_path{path_idx}.py"
                with open(test_file, "w", encoding="utf-8") as f:
                    f.write(f"# Method: PAST\n")
                    f.write(f"# Target file: {self.target_file}\n")
                    f.write(f"# Condition path: {path['condition']}\n")
                    f.write(f"# Repetition: {rep_idx}, Iteration: {iter_idx}\n")
                    f.write(f"# Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("\n")
                    f.write(code)
                print(f"        [SAVE] Saved: {test_file}")

                try:
                    ast.parse(code)
                    print(f"        [OK] Code syntax is correct")
                    return code
                except SyntaxError as e:
                    print(f"        [WARN] Syntax error: {e}")
                    continue

            except Exception as e:
                print(f"        [WARN] API failed: {e}")
                time.sleep(2)
                continue

        print(f"        [FAIL] Generation failed, using fallback test")
        return self._generate_fallback_test(path)

    def _generate_fallback_test(self, path: dict) -> str:
        """Generate fallback test (without API dependency)"""
        return f'''
import pytest
from {self.module_name} import {self.function_name}

@pytest.mark.parametrize("input_text", [
    "  hello",
    "    line1\\n      line2",
    "no indent",
    "",
    "  ",
])
def test_target_path(input_text):
    result = {self.function_name}(input_text)
    assert isinstance(result, str)
'''

    def _extract_code(self, content: str) -> str:
        """Extract code block - supports ``` format"""
        patterns = [
            r'\^\^\^python(.*?)\^\^\^',
            r'\^\^\^(.*?)\^\^\^',
            r'```python(.*?)```',
            r'```(.*?)```',
            r'(import pytest.*?)(?=\n\n|\Z)',
        ]

        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                return match.group(1).strip()

        if 'import pytest' in content:
            return content.strip()

        return ""

    def _fix_code(self, code: str) -> str:
        """Fix common code issues"""
        # If code redefines the function, forcibly remove it
        lines = code.split('\n')
        new_lines = []
        skip_until_indent = False

        for line in lines:
            # Detect function redefinition
            if f'def {self.function_name}' in line and 'from ' not in code:
                skip_until_indent = True
                new_lines.append(f'from {self.module_name} import {self.function_name}')
                continue

            if skip_until_indent:
                if line and not line.startswith(' ') and not line.startswith('\t'):
                    skip_until_indent = False
                else:
                    continue

            new_lines.append(line)

        code = '\n'.join(new_lines)

        # Ensure import exists
        if f'from {self.module_name}' not in code and f'import {self.module_name}' not in code:
            code = f'from {self.module_name} import {self.function_name}\n' + code

        return code

    def run(self, max_iter: int = 15, rep_idx: int = 0) -> dict:
        """Run PAST method (UCB strategy support)"""

        condition_path_history = []
        effective_history = []
        line_history = []
        branch_history = []

        covered_conds = [False] * len(self.paths)
        fail_count = [0] * len(self.paths)

        executor = TestExecutor(self.target_file, prefix=f"past_rep{rep_idx}_")

        print(f"  [INFO] Total effective lines: {len(self.coverage_analyzer.effective_lines)}")

        # UCB status prompt
        if self.use_ucb:
            print(f"  [UCB] UCB strategy enabled, mode={self.ucb_mode}, exploration parameter c={self.ucb_c}")
            self.previous_effective_cov = 0
            self.ucb_stats.reset()
        else:
            print(f"  [UCB] Using original PAST strategy (priority selection)")

        for i in range(max_iter):
            print(f"      [ITER] Iteration {i + 1}/{max_iter}: Starting...")

            # ========== Path Selection ==========
            if self.use_ucb:
                selected_idx = self._select_path_ucb(covered_conds, fail_count)
            else:
                selected_idx = self._select_path_original(covered_conds, fail_count)

            # If no available path (all conditions covered or cannot be covered)
            if selected_idx is None:
                condition_cov = self._get_condition_coverage(covered_conds)
                # Fill remaining iterations with historical records
                for j in range(i, max_iter):
                    condition_path_history.append(condition_cov)
                    effective_history.append(effective_history[-1] if effective_history else 0)
                    line_history.append(line_history[-1] if line_history else 0)
                    branch_history.append(branch_history[-1] if branch_history else 0)
                print(f"      [ITER] All conditions covered or cannot continue (condition coverage={condition_cov:.1f}%), stopping early")
                break

            path = self.paths[selected_idx]
            print(f"      [ITER] Iteration {i + 1}/{max_iter}: Target condition: {path['condition'][:50]}...")

            test_code = self._generate_test_for_path(path, rep_idx=rep_idx, iter_idx=i, path_idx=selected_idx)

            if not test_code:
                fail_count[selected_idx] += 1
                # UCB: Record failure
                if self.use_ucb:
                    self.ucb_stats.update(selected_idx, False, reward=0)
                condition_path_history.append(self._get_condition_coverage(covered_conds))
                effective_history.append(effective_history[-1] if effective_history else 0)
                line_history.append(line_history[-1] if line_history else 0)
                branch_history.append(branch_history[-1] if branch_history else 0)
                continue

            try:
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as executor_pool:
                    future = executor_pool.submit(executor.run, test_code, i)
                    try:
                        success, line_cov, branch_cov, covered_lines = future.result(timeout=20)

                        # Debug output
                        print(f"        [DEBUG] Covered lines: {covered_lines}")
                        print(f"        [DEBUG] Effective lines set: {self.coverage_analyzer.effective_lines}")
                        print(f"        [DEBUG] Effective covered lines: {covered_lines & self.coverage_analyzer.effective_lines}")

                    except concurrent.futures.TimeoutError:
                        print(f"        [TIMEOUT] Test execution timeout (20 seconds)")
                        success = False
                        line_cov = 0
                        branch_cov = 0
                        covered_lines = set()
                    except Exception as e:
                        print(f"        [ERROR] Execution exception: {e}")
                        success = False
                        line_cov = 0
                        branch_cov = 0
                        covered_lines = set()
            except ImportError:
                try:
                    success, line_cov, branch_cov, covered_lines = executor.run(test_code, i)

                    # Debug output
                    print(f"        [DEBUG] Covered lines: {covered_lines}")
                    print(f"        [DEBUG] Effective lines set: {self.coverage_analyzer.effective_lines}")
                    print(f"        [DEBUG] Effective covered lines: {covered_lines & self.coverage_analyzer.effective_lines}")

                except Exception as e:
                    print(f"        [ERROR] Execution failed: {e}")
                    success = False
                    line_cov = 0
                    branch_cov = 0
                    covered_lines = set()

            # ========== UCB: Calculate coverage gain as reward ==========
            if self.use_ucb:
                coverage_gain = max(0, line_cov - self.previous_effective_cov)
                self.previous_effective_cov = line_cov

            if line_cov > 0:  # Test executed code, consider success
                print(f"        [DEBUG] Line coverage={line_cov}% > 0, marking condition as covered")
                if not covered_conds[selected_idx]:
                    covered_conds[selected_idx] = True
                effective_cov = line_cov
                if effective_cov > self.best_effective_cov:
                    self.best_effective_cov = effective_cov
                    self.best_test_code = test_code

                # UCB: Record success and reward
                if self.use_ucb:
                    self.ucb_stats.update(selected_idx, True, reward=coverage_gain)
            else:
                fail_count[selected_idx] += 1
                effective_cov = 0
                # UCB: Record failure
                if self.use_ucb:
                    self.ucb_stats.update(selected_idx, False, reward=0)

            # Print current coverage status
            print(f"        [DEBUG] Current condition coverage status: {covered_conds}")

            condition_cov = self._get_condition_coverage(covered_conds)
            condition_path_history.append(condition_cov)
            effective_history.append(effective_cov)
            line_history.append(line_cov)
            branch_history.append(branch_cov)

            print(f"      [ITER] Iteration {i + 1}/{max_iter}: Condition path={condition_cov:.1f}%, "
                  f"Effective coverage={effective_cov:.1f}%, Line coverage={line_cov:.1f}%")

            time.sleep(1)

        executor.cleanup()

        # ========== UCB: Save statistics ==========
        if self.use_ucb:
            os.makedirs("ucb_stats", exist_ok=True)
            stats_file = f"ucb_stats/past_ucb_{self.module_name}_rep{rep_idx}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            self.ucb_stats.save_stats(stats_file)
            print(f"  [UCB] Statistics saved: {stats_file}")

        return {
            'condition_path_history': condition_path_history,
            'effective_history': effective_history,
            'line_history': line_history,
            'branch_history': branch_history
        }

    def _improve_test(self, current_test: str) -> str:
        """Improve existing test"""
        prompt = f"""Current test coverage is insufficient. Please improve the test code by adding more test cases.

Current test:
```python
{current_test}
```

Target function:
```python
{self.source}
```

Requirements:
1. Add more test cases to cover different scenarios
2. Add more detailed assertions
3. Ensure the test executes the core logic of the function

Please output the complete improved test code:
"""
        try:
            resp = self.client.chat.completions.create(
                model="qwen-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                timeout=30
            )
            content = resp.choices[0].message.content
            code = self._extract_code(content)
            if code:
                return self._fix_code(code)
        except:
            pass

        return current_test

    def _get_condition_coverage(self, covered_conds: list) -> float:
        return sum(covered_conds) / len(covered_conds) * 100 if covered_conds else 0