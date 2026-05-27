# methods/pure_llm_method.py
# Pure LLM Method - LLM directly generates tests

import os
import re
import ast
import time
from openai import OpenAI
from common.test_executor import TestExecutor
from common.coverage_analyzer import CoverageAnalyzer


class PureLLMMethod:
    """Pure LLM Method"""

    def __init__(self, target_file: str, api_key: str = None, base_url: str = None):
        self.target_file = target_file
        self.source = open(target_file, encoding='utf-8').read()
        self.module_name = os.path.splitext(os.path.basename(target_file))[0]
        self.function_name = self._extract_function_name()

        self.api_key = api_key or "sk-f0df09ba45bf458dacd7dbe1367c16db"
        self.base_url = base_url or "https://dashscope.aliyuncs.com/compatible-mode/v1"
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

        self.coverage_analyzer = CoverageAnalyzer(target_file)
        self.cached_test_code = None

    def _extract_function_name(self) -> str:
        try:
            tree = ast.parse(self.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    return node.name
            return os.path.splitext(os.path.basename(self.target_file))[0]
        except:
            return "target_function"

    def _generate_test_code(self, iteration: int) -> str:
        prompt = f"""
You are a white-box testing expert.

Target code ({self.module_name}.py):
```python
{self.source}
```

Target function name: {self.function_name}

Task:
Generate a comprehensive pytest test function that covers all branches.

Requirements:
1. Function name must be test_pure_llm_iter{iteration}
2. Use @pytest.mark.parametrize
3. Call the target function {self.function_name}
4. Cover all return values
5. Output format must be wrapped in python code blocks using ```python and ```
"""

        for attempt in range(3):
            try:
                resp = self.client.chat.completions.create(
                    model="qwen-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3,
                    timeout=30
                )

                code = resp.choices[0].message.content
                # Support both ``` and ``` formats
                match = re.search(r'\^\^\^python(.*?)\^\^\^', code, re.DOTALL)
                if not match:
                    match = re.search(r'```python(.*?)```', code, re.DOTALL)
                code = match.group(1).strip() if match else code.strip()

                try:
                    ast.parse(code)
                    return code
                except SyntaxError:
                    continue

            except Exception:
                time.sleep(1)
                continue

        return ""

    def run(self, max_iter: int = 15, rep_idx: int = 0) -> dict:
        effective_history = []
        line_history = []
        branch_history = []

        executor = TestExecutor(self.target_file, prefix=f"purellm_rep{rep_idx}_")

        for i in range(max_iter):
            if i == 0 or self.cached_test_code is None:
                test_code = self._generate_test_code(i)
                if test_code:
                    self.cached_test_code = test_code
            else:
                test_code = self.cached_test_code

            if test_code:
                success, line_cov, branch_cov, covered_lines = executor.run(test_code, i)
                effective_cov = self.coverage_analyzer.compute_effective_coverage(covered_lines)
            else:
                effective_cov = effective_history[-1] if effective_history else 0
                line_cov = line_history[-1] if line_history else 0
                branch_cov = branch_history[-1] if branch_history else 0

            effective_history.append(effective_cov)
            line_history.append(line_cov)
            branch_history.append(branch_cov)

            print(f"     Iteration {i+1}/{max_iter}: Effective coverage={effective_cov:.1f}%")

        executor.cleanup()

        return {
            'effective_history': effective_history,
            'line_history': line_history,
            'branch_history': branch_history
        }