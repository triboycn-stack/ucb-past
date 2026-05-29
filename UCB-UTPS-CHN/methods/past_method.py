# methods/past_method.py
"""PAST方法 - 改进版，提高有效覆盖率（支持UCB策略）"""

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


# ========== UCB统计管理器 ==========
class UCBStats:
    """UCB统计信息管理器"""

    def __init__(self):
        self.total_count = 0
        self.path_stats = {}  # {path_idx: {'success': int, 'fail': int, 'reward': float, 'total_tries': int}}

    def reset(self):
        """重置统计信息"""
        self.total_count = 0
        self.path_stats = {}

    def update(self, path_idx: int, success: bool, reward: float = None):
        """更新路径统计"""
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
        """获取路径的成功率"""
        key = str(path_idx)
        stats = self.path_stats.get(key, {'total_tries': 0, 'success': 0})
        total = stats['total_tries']
        if total == 0:
            return 0.5  # 初始乐观估计
        return stats['success'] / total

    def get_reward(self, path_idx: int) -> float:
        """获取平均奖励"""
        key = str(path_idx)
        stats = self.path_stats.get(key, {'reward': 0, 'total_tries': 0})
        if stats['total_tries'] == 0:
            return 0.0
        return stats['reward']

    def get_try_count(self, path_idx: int) -> int:
        """获取尝试次数"""
        key = str(path_idx)
        stats = self.path_stats.get(key, {'total_tries': 0})
        return stats['total_tries']

    def calculate_ucb(self, path_idx: int, c: float = 1.414) -> float:
        """
        计算UCB值
        UCB = average_reward + c * sqrt(ln(total_tries) / n_i)
        """
        success_rate = self.get_success_rate(path_idx)
        n_i = self.get_try_count(path_idx)

        if n_i == 0:
            return float('inf')

        exploration_bonus = c * math.sqrt(math.log(self.total_count + 1) / n_i)
        return success_rate + exploration_bonus

    def calculate_ucb_tuned(self, path_idx: int, c: float = 1.414) -> float:
        """UCB-Tuned变体"""
        success_rate = self.get_success_rate(path_idx)
        n_i = self.get_try_count(path_idx)

        if n_i == 0:
            return float('inf')

        variance = success_rate * (1 - success_rate)
        exploration_bonus = math.sqrt((math.log(self.total_count + 1) / n_i) *
                                      min(0.25, variance + math.sqrt(2 * math.log(self.total_count + 1) / n_i)))
        return success_rate + c * exploration_bonus

    def save_stats(self, filename: str):
        """保存统计信息"""
        stats_data = {
            'total_count': self.total_count,
            'path_stats': self.path_stats
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(stats_data, f, indent=2)

    def load_stats(self, filename: str):
        """加载统计信息"""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.total_count = data.get('total_count', 0)
                self.path_stats = data.get('path_stats', {})
            return True
        return False


class PASTMethod:
    """PAST方法 - 改进版（支持UCB策略）"""

    def __init__(self, target_file: str, api_key: str = None, base_url: str = None):
        self.target_file = target_file
        self.source = open(target_file, encoding='utf-8').read()
        self.module_name = os.path.splitext(os.path.basename(target_file))[0]
        self.function_name = self._extract_function_name()
        self.params = self._extract_params()
        self.coverage_analyzer = CoverageAnalyzer(target_file)

        # 提取条件路径
        self.paths = self._extract_paths()

        # 初始化LLM客户端
        self.api_key = api_key or "sk-f0df09ba45bf458dacd7dbe1367c16db"
        self.base_url = base_url or "https://dashscope.aliyuncs.com/compatible-mode/v1"
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

        # 缓存
        self.generated_tests = set()
        self.best_test_code = None
        self.best_effective_cov = 0

        # ========== UCB相关属性 ==========
        self.use_ucb = False  # 是否使用UCB策略，默认False保持原有行为
        self.ucb_mode = 'standard'  # 'standard', 'tuned'
        self.ucb_stats = UCBStats()
        self.ucb_c = 1.414  # 探索参数
        self.previous_effective_cov = 0  # 用于计算奖励

    # ========== UCB配置方法 ==========
    def enable_ucb(self, c: float = 1.414, mode: str = 'standard'):
        """启用UCB策略"""
        self.use_ucb = True
        self.ucb_c = c
        self.ucb_mode = mode
        self.ucb_stats.reset()
        self.previous_effective_cov = 0
        print(f"  [UCB] 已启用，模式={mode}, 探索参数 c={c}")

    def disable_ucb(self):
        """禁用UCB策略，恢复原始PAST行为"""
        self.use_ucb = False
        print(f"  [UCB] 已禁用，恢复原始PAST策略")

    def _select_path_ucb(self, covered_conds: list, fail_count: list) -> int:
        """
        UCB路径选择策略
        选择UCB值最大的未覆盖路径
        返回: 选中的路径索引，如果没有可用路径则返回None
        """
        candidates = []

        for idx in range(len(self.paths)):
            # 跳过已覆盖的
            if covered_conds[idx]:
                continue

            # 跳过失败次数过多的
            if fail_count[idx] >= 3:
                continue

            # 计算UCB值
            if self.ucb_mode == 'tuned':
                ucb_value = self.ucb_stats.calculate_ucb_tuned(idx, self.ucb_c)
            else:
                ucb_value = self.ucb_stats.calculate_ucb(idx, self.ucb_c)
            candidates.append((idx, ucb_value))

        if not candidates:
            # 如果没有候选，尝试重置失败计数
            for idx in range(len(self.paths)):
                if not covered_conds[idx]:
                    fail_count[idx] = 0
                    if self.ucb_mode == 'tuned':
                        ucb_value = self.ucb_stats.calculate_ucb_tuned(idx, self.ucb_c)
                    else:
                        ucb_value = self.ucb_stats.calculate_ucb(idx, self.ucb_c)
                    candidates.append((idx, ucb_value))

            # 仍然没有候选，说明所有条件都已覆盖
            if not candidates:
                return None

        # 按UCB值降序排序，选择最大值
        candidates.sort(key=lambda x: x[1], reverse=True)
        selected_idx = candidates[0][0]

        print(f"        [UCB] 选择路径 {selected_idx}, UCB={candidates[0][1]:.4f}, "
              f"尝试次数={self.ucb_stats.get_try_count(selected_idx)}")

        return selected_idx

    def _select_path_original(self, covered_conds: list, fail_count: list) -> int:
        """
        原始PAST路径选择策略（保持不变）
        优先选择未覆盖且失败次数小于3的条件
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
        """提取函数参数"""
        try:
            tree = ast.parse(self.source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == self.function_name:
                    return [arg.arg for arg in node.args.args]
        except:
            pass
        return []

    def _extract_paths(self) -> list:
        """提取条件路径"""
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

        # 去重
        unique_paths = []
        seen = set()
        for p in paths:
            cond = p["condition"]
            if cond not in seen:
                seen.add(cond)
                unique_paths.append(p)

        unique_paths.sort(key=lambda x: (-x["priority"], x["condition"]))

        print(f"  [INFO] 提取到 {len(unique_paths)} 条条件路径")
        print(f"  [INFO] 函数参数: {self.params}")
        return unique_paths

    def _generate_param_examples(self) -> str:
        """生成参数示例"""
        if not self.params:
            return "无参数"

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
        """为特定条件路径生成高质量的测试"""

        params_example = self._generate_param_examples()

        prompt = f"""你是白盒测试专家。生成一个能够执行目标代码核心逻辑的pytest测试。

        ## 目标代码（需要测试的代码）
        文件: {self.module_name}.py
        ```python
        {self.source}
        ```

        ## 目标函数
        - 函数名: {self.function_name}
        - 参数: {self.params}
        - 参数示例: {params_example}

        ## 目标条件路径
        需要覆盖的条件: {path['condition']}

        ## 重要规则（必须遵守）

        1. **必须导入原始函数**，不要重新定义：
           ```python
           from {self.module_name} import {self.function_name}
           ```

        2. **禁止**在测试函数内部重新定义目标函数

        3. 测试必须执行函数的**核心逻辑**，不能只是简单返回

        4. 使用 @pytest.mark.parametrize 提供多个测试用例

        ## ⚠️ 测试深度要求（非常重要）

        1. **不仅要测试返回值，还要测试内部状态变化**
        2. **对于条件分支，每个分支都要有对应的测试用例**
        3. **对于循环，测试空集合、单元素、多元素情况**
        4. **对于边界条件，测试最小值、最大值、临界值**
        5. **对于异常情况，测试非法输入和错误处理**

        ## 正确示例
        ```python
        import pytest
        from {self.module_name} import {self.function_name}

        # 示例：测试标识符验证函数
        @pytest.mark.parametrize("name,expected", [
            # 有效标识符
            ("validName", True),
            ("_private", True),
            ("$dollar", True),
            ("a1b2c3", True),
            # 无效标识符（开头错误）
            ("123invalid", False),
            ("1var", False),
            # 保留字
            ("class", False),
            ("return", False),
            ("if", False),
            # 边界情况
            ("", False),
            ("a", True),
            ("x" * 100, True),  # 长字符串
        ])
        def test_target_path(name, expected):
            result = {self.function_name}(name)
            assert result == expected
        ```

        请只输出Python代码，不要有其他解释：
        """

        for attempt in range(max_retries):
            try:
                print(f"        [API] 调用API生成测试 (尝试 {attempt + 1}/{max_retries})...")
                resp = self.client.chat.completions.create(
                    model="qwen-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3,
                    timeout=60
                )

                content = resp.choices[0].message.content
                code = self._extract_code(content)

                if not code:
                    print(f"        [WARN] 无法提取代码")
                    continue

                # 检查是否包含错误的重新定义
                if f'def {self.function_name}' in code and 'from ' not in code:
                    print(f"        [WARN] 检测到函数重新定义，拒绝使用")
                    continue

                code = self._fix_code(code)

                # 保存生成的测试代码
                os.makedirs("generated_tests", exist_ok=True)
                test_file = f"generated_tests/PAST_{self.module_name}_rep{rep_idx}_iter{iter_idx}_path{path_idx}.py"
                with open(test_file, "w", encoding="utf-8") as f:
                    f.write(f"# 方法: PAST\n")
                    f.write(f"# 目标文件: {self.target_file}\n")
                    f.write(f"# 条件路径: {path['condition']}\n")
                    f.write(f"# 重复次数: {rep_idx}, 迭代: {iter_idx}\n")
                    f.write(f"# 生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("\n")
                    f.write(code)
                print(f"        [SAVE] 已保存: {test_file}")

                try:
                    ast.parse(code)
                    print(f"        [OK] 代码语法正确")
                    return code
                except SyntaxError as e:
                    print(f"        [WARN] 语法错误: {e}")
                    continue

            except Exception as e:
                print(f"        [WARN] API失败: {e}")
                time.sleep(2)
                continue

        print(f"        [FAIL] 生成失败，使用回退测试")
        return self._generate_fallback_test(path)

    def _generate_fallback_test(self, path: dict) -> str:
        """生成回退测试（不依赖API）"""
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
        """提取代码块 - 支持```格式"""
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
        """修复常见代码问题"""
        # 如果代码中重新定义了函数，强制删除
        lines = code.split('\n')
        new_lines = []
        skip_until_indent = False

        for line in lines:
            # 检测函数重新定义
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

        # 确保导入存在
        if f'from {self.module_name}' not in code and f'import {self.module_name}' not in code:
            code = f'from {self.module_name} import {self.function_name}\n' + code

        return code

    def run(self, max_iter: int = 15, rep_idx: int = 0) -> dict:
        """运行PAST方法（支持UCB策略）"""

        condition_path_history = []
        effective_history = []
        line_history = []
        branch_history = []

        covered_conds = [False] * len(self.paths)
        fail_count = [0] * len(self.paths)

        executor = TestExecutor(self.target_file, prefix=f"past_rep{rep_idx}_")

        print(f"  [INFO] 有效行总数: {len(self.coverage_analyzer.effective_lines)}")

        # UCB状态提示
        if self.use_ucb:
            print(f"  [UCB] UCB策略已启用，模式={self.ucb_mode}, 探索参数 c={self.ucb_c}")
            self.previous_effective_cov = 0
            self.ucb_stats.reset()
        else:
            print(f"  [UCB] 使用原始PAST策略（优先级选择）")

        for i in range(max_iter):
            print(f"      [ITER] 迭代 {i + 1}/{max_iter}: 开始...")

            # ========== 路径选择 ==========
            if self.use_ucb:
                selected_idx = self._select_path_ucb(covered_conds, fail_count)
            else:
                selected_idx = self._select_path_original(covered_conds, fail_count)

            # 如果没有可用路径（所有条件已覆盖或无法覆盖）
            if selected_idx is None:
                condition_cov = self._get_condition_coverage(covered_conds)
                # 填充剩余迭代的历史记录
                for j in range(i, max_iter):
                    condition_path_history.append(condition_cov)
                    effective_history.append(effective_history[-1] if effective_history else 0)
                    line_history.append(line_history[-1] if line_history else 0)
                    branch_history.append(branch_history[-1] if branch_history else 0)
                print(f"      [ITER] 所有条件已覆盖或无法继续 (条件覆盖={condition_cov:.1f}%)，提前结束")
                break

            path = self.paths[selected_idx]
            print(f"      [ITER] 迭代 {i + 1}/{max_iter}: 目标条件: {path['condition'][:50]}...")

            test_code = self._generate_test_for_path(path, rep_idx=rep_idx, iter_idx=i, path_idx=selected_idx)

            if not test_code:
                fail_count[selected_idx] += 1
                # UCB: 记录失败
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

                        # 调试输出
                        print(f"        [DEBUG] 覆盖的行号: {covered_lines}")
                        print(f"        [DEBUG] 有效行集合: {self.coverage_analyzer.effective_lines}")
                        print(f"        [DEBUG] 有效覆盖行: {covered_lines & self.coverage_analyzer.effective_lines}")

                    except concurrent.futures.TimeoutError:
                        print(f"        [TIMEOUT] 测试执行超时 (20秒)")
                        success = False
                        line_cov = 0
                        branch_cov = 0
                        covered_lines = set()
                    except Exception as e:
                        print(f"        [ERROR] 执行异常: {e}")
                        success = False
                        line_cov = 0
                        branch_cov = 0
                        covered_lines = set()
            except ImportError:
                try:
                    success, line_cov, branch_cov, covered_lines = executor.run(test_code, i)

                    # 调试输出
                    print(f"        [DEBUG] 覆盖的行号: {covered_lines}")
                    print(f"        [DEBUG] 有效行集合: {self.coverage_analyzer.effective_lines}")
                    print(f"        [DEBUG] 有效覆盖行: {covered_lines & self.coverage_analyzer.effective_lines}")

                except Exception as e:
                    print(f"        [ERROR] 执行失败: {e}")
                    success = False
                    line_cov = 0
                    branch_cov = 0
                    covered_lines = set()

            # ========== UCB: 计算覆盖率增益作为奖励 ==========
            if self.use_ucb:
                coverage_gain = max(0, line_cov - self.previous_effective_cov)
                self.previous_effective_cov = line_cov

            if line_cov > 0:  # 只要测试执行了代码就算成功
                print(f"        [DEBUG] 行覆盖率={line_cov}% > 0, 标记条件已覆盖")
                if not covered_conds[selected_idx]:
                    covered_conds[selected_idx] = True
                effective_cov = line_cov
                if effective_cov > self.best_effective_cov:
                    self.best_effective_cov = effective_cov
                    self.best_test_code = test_code

                # UCB: 记录成功和奖励
                if self.use_ucb:
                    self.ucb_stats.update(selected_idx, True, reward=coverage_gain)
            else:
                fail_count[selected_idx] += 1
                effective_cov = 0
                # UCB: 记录失败
                if self.use_ucb:
                    self.ucb_stats.update(selected_idx, False, reward=0)

            # 打印当前覆盖状态
            print(f"        [DEBUG] 当前条件覆盖状态: {covered_conds}")

            condition_cov = self._get_condition_coverage(covered_conds)
            condition_path_history.append(condition_cov)
            effective_history.append(effective_cov)
            line_history.append(line_cov)
            branch_history.append(branch_cov)

            print(f"      [ITER] 迭代 {i + 1}/{max_iter}: 条件路径={condition_cov:.1f}%, "
                  f"有效覆盖={effective_cov:.1f}%, 行覆盖={line_cov:.1f}%")

            time.sleep(1)

        executor.cleanup()

        # ========== UCB: 保存统计信息 ==========
        if self.use_ucb:
            os.makedirs("ucb_stats", exist_ok=True)
            stats_file = f"ucb_stats/past_ucb_{self.module_name}_rep{rep_idx}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            self.ucb_stats.save_stats(stats_file)
            print(f"  [UCB] 统计已保存: {stats_file}")

        return {
            'condition_path_history': condition_path_history,
            'effective_history': effective_history,
            'line_history': line_history,
            'branch_history': branch_history
        }

    def _improve_test(self, current_test: str) -> str:
        """改进现有测试"""
        prompt = f"""当前测试覆盖率不足，请改进测试代码，增加更多测试用例。

当前测试：
```python
{current_test}
```

目标函数：
```python
{self.source}
```

要求：
1. 增加更多测试用例覆盖不同情况
2. 添加更详细的断言
3. 确保测试能执行函数的核心逻辑

请输出改进后的完整测试代码：
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