# methods/no_healing_method.py
"""No-Healing Method - Ablation Study: Random Condition Selection without Feedback"""

import random
from methods.past_method import PASTMethod
from common.test_executor import TestExecutor
from common.coverage_analyzer import CoverageAnalyzer


class NoHealingMethod(PASTMethod):
    """No-Healing Method - Random condition selection without feedback mechanism"""

    def __init__(self, target_file: str, api_key: str = None, base_url: str = None):
        super().__init__(target_file, api_key, base_url)
        print(f"  [INFO] No-Healing Mode: Random condition selection, no feedback")

    def run(self, max_iter: int = 15, rep_idx: int = 0) -> dict:
        """Run No-Healing method - Random condition selection without adjustment based on coverage status"""

        condition_path_history = []
        effective_history = []
        line_history = []
        branch_history = []

        # Record coverage status only, not used for selection (feedback mechanism ablated)
        covered_conds = [False] * len(self.paths)
        fail_count = [0] * len(self.paths)

        executor = TestExecutor(self.target_file, prefix=f"noheal_rep{rep_idx}_")

        print(f"  [INFO] Total effective lines: {len(self.coverage_analyzer.effective_lines)}")

        for i in range(max_iter):
            print(f"      [ITER] Iteration {i + 1}/{max_iter}: Starting...")

            # ========== Key difference: Random condition selection (priority and feedback ablated) ==========
            selected_idx = random.randint(0, len(self.paths) - 1)
            # ================================================================================================

            path = self.paths[selected_idx]
            print(f"      [ITER] Iteration {i + 1}/{max_iter}: Randomly selected condition {selected_idx}: {path['condition'][:50]}...")

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

                        # Debug output
                        print(f"        [DEBUG] Number of covered lines: {len(covered_lines)}")

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
                except Exception as e:
                    print(f"        [ERROR] Execution failed: {e}")
                    success = False
                    line_cov = 0
                    branch_cov = 0
                    covered_lines = set()

            # Record coverage status (but not used to guide subsequent selection)
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

            print(f"      [ITER] Iteration {i + 1}/{max_iter}: Condition Path = {condition_cov:.1f}%, "
                  f"Effective Coverage = {effective_cov:.1f}%, Line Coverage = {line_cov:.1f}%")

            # Avoid API call rate limiting
            import time
            time.sleep(1)

        executor.cleanup()

        return {
            'condition_path_history': condition_path_history,
            'effective_history': effective_history,
            'line_history': line_history,
            'branch_history': branch_history
        }