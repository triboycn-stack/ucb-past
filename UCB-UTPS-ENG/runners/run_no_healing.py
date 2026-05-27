# runners/run_no_healing.py
# !/usr/bin/env python3
"""独立运行No-Healing方法（消融实验）"""

import sys
import os

# 设置控制台编码为UTF-8
if sys.platform == 'win32':
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import numpy as np
from datetime import datetime
from methods.no_healing_method import NoHealingMethod
from common.data_structures import ExperimentResult


def run_no_healing_experiment(target_file: str, repetitions: int = 5, max_iter: int = 15):
    print(f"\n{'=' * 60}")
    print(f"[No-Healing] No-Healing方法实验（消融实验）")
    print(f"   目标: {target_file}, 重复: {repetitions}, 迭代: {max_iter}")
    print(f"{'=' * 60}")

    all_cond = []
    all_effective = []
    all_line = []
    all_branch = []

    final_cond = []
    final_effective = []
    final_line = []
    final_branch = []

    for rep in range(repetitions):
        print(f"\n[重复] 第 {rep + 1}/{repetitions} 次")
        method = NoHealingMethod(target_file)
        result = method.run(max_iter=max_iter, rep_idx=rep)

        all_cond.append(result['condition_path_history'])
        all_effective.append(result['effective_history'])
        all_line.append(result['line_history'])
        all_branch.append(result['branch_history'])

        final_cond.append(result['condition_path_history'][-1])
        final_effective.append(result['effective_history'][-1])
        final_line.append(result['line_history'][-1])
        final_branch.append(result['branch_history'][-1])

    exp_result = ExperimentResult(
        method_name='No-Healing',
        target_file=target_file,
        repetitions=repetitions,
        max_iter=max_iter,
        timestamp=datetime.now().strftime("%Y%m%d_%H%M%S"),
        condition_path_coverage_history=all_cond,
        final_condition_path_coverage=final_cond,
        effective_line_coverage_history=all_effective,
        final_effective_coverage=final_effective,
        line_coverage_history=all_line,
        final_line_coverage=final_line,
        branch_coverage_history=all_branch,
        final_branch_coverage=final_branch
    )

    os.makedirs("results", exist_ok=True)
    out_file = f"results/no_healing_{os.path.basename(target_file)}_{exp_result.timestamp}.json"
    exp_result.save(out_file)

    print(f"\n[完成] 条件路径: {np.mean(final_cond):.1f}% ± {np.std(final_cond):.1f}%")
    print(f"[保存] {out_file}")
    return exp_result


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "target4_dedent.py"
    reps = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    iters = int(sys.argv[3]) if len(sys.argv) > 3 else 15
    run_no_healing_experiment(target, reps, iters)