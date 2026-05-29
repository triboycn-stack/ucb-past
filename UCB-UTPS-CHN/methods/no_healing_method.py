# methods/no_healing_method.py
"""No-Healing方法 - 消融实验：随机选择条件，无反馈"""

import random
from methods.past_method import PASTMethod
from common.test_executor import TestExecutor
from common.coverage_analyzer import CoverageAnalyzer


class NoHealingMethod(PASTMethod):
    """No-Healing方法 - 随机条件选择，无反馈机制"""

    def __init__(self, target_file: str, api_key: str = None, base_url: str = None):
        super().__init__(target_file, api_key, base_url)
        print(f"  [INFO] No-Healing模式: 随机选择条件，无反馈")

    def run(self, max_iter: int = 15, rep_idx: int = 0) -> dict:
        """运行No-Healing方法 - 随机选择条件，不根据覆盖状态调整"""

        condition_path_history = []
        effective_history = []
        line_history = []
        branch_history = []

        # 只记录覆盖状态，但不用于选择（消融掉反馈机制）
        covered_conds = [False] * len(self.paths)
        fail_count = [0] * len(self.paths)

        executor = TestExecutor(self.target_file, prefix=f"noheal_rep{rep_idx}_")

        print(f"  [INFO] 有效行总数: {len(self.coverage_analyzer.effective_lines)}")

        for i in range(max_iter):
            print(f"      [ITER] 迭代 {i + 1}/{max_iter}: 开始...")

            # ========== 关键区别：随机选择条件（消融掉优先级和反馈） ==========
            selected_idx = random.randint(0, len(self.paths) - 1)
            # ==================================================================

            path = self.paths[selected_idx]
            print(f"      [ITER] 迭代 {i + 1}/{max_iter}: 随机选择条件 {selected_idx}: {path['condition'][:50]}...")

            test_code = self._generate_test_for_path(path, rep_idx=rep_idx, iter_idx=i, path_idx=selected_idx)

            if not test_code:
                fail_count[selected_idx] += 1
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
                        print(f"        [DEBUG] 覆盖的行号数: {len(covered_lines)}")

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
                except Exception as e:
                    print(f"        [ERROR] 执行失败: {e}")
                    success = False
                    line_cov = 0
                    branch_cov = 0
                    covered_lines = set()

            # 记录覆盖状态（但不用于指导后续选择）
            if success and line_cov > 0:
                if not covered_conds[selected_idx]:
                    covered_conds[selected_idx] = True
                effective_cov = line_cov
            else:
                fail_count[selected_idx] += 1
                effective_cov = 0

            condition_cov = self._get_condition_coverage(covered_conds)
            condition_path_history.append(condition_cov)
            effective_history.append(effective_cov)
            line_history.append(line_cov)
            branch_history.append(branch_cov)

            print(f"      [ITER] 迭代 {i + 1}/{max_iter}: 条件路径={condition_cov:.1f}%, "
                  f"有效覆盖={effective_cov:.1f}%, 行覆盖={line_cov:.1f}%")

            # 避免API调用过快
            import time
            time.sleep(1)

        executor.cleanup()

        return {
            'condition_path_history': condition_path_history,
            'effective_history': effective_history,
            'line_history': line_history,
            'branch_history': branch_history
        }