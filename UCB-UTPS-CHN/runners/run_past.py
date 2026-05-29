# runners/run_past.py
# !/usr/bin/env python3
"""独立运行PAST方法（支持UCB策略）"""

import sys
import os
import argparse

# 设置控制台编码为UTF-8
if sys.platform == 'win32':
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import numpy as np
from datetime import datetime
from methods.past_method import PASTMethod
from common.data_structures import ExperimentResult


def run_past_experiment(target_file: str, repetitions: int = 5, max_iter: int = 15,
                        use_ucb: bool = False, ucb_c: float = 1.414, ucb_mode: str = 'standard'):
    """
    运行PAST实验

    Args:
        target_file: 目标文件路径
        repetitions: 重复次数
        max_iter: 最大迭代次数
        use_ucb: 是否使用UCB策略
        ucb_c: UCB探索参数
        ucb_mode: UCB模式 ('standard' 或 'tuned')
    """
    method_name = "PAST-UCB" if use_ucb else "PAST"
    print(f"\n{'=' * 60}")
    print(f"[{method_name}] {method_name}方法实验")
    print(f"   目标: {target_file}, 重复: {repetitions}, 迭代: {max_iter}")
    if use_ucb:
        print(f"   UCB: 模式={ucb_mode}, 探索参数 c={ucb_c}")
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
        method = PASTMethod(target_file)

        # 配置UCB
        if use_ucb:
            method.enable_ucb(c=ucb_c, mode=ucb_mode)

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
        method_name=method_name,
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
    method_suffix = "_ucb" if use_ucb else ""
    out_file = f"results/past{method_suffix}_{os.path.basename(target_file)}_{exp_result.timestamp}.json"
    exp_result.save(out_file)

    print(f"\n[完成] {method_name} 条件路径: {np.mean(final_cond):.1f}% ± {np.std(final_cond):.1f}%")
    print(f"[完成] {method_name} 有效行覆盖: {np.mean(final_effective):.1f}% ± {np.std(final_effective):.1f}%")
    print(f"[保存] {out_file}")
    return exp_result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='运行PAST方法实验')
    parser.add_argument('target', type=str, help='目标文件路径')
    parser.add_argument('repetitions', type=int, nargs='?', default=5, help='重复次数 (默认: 5)')
    parser.add_argument('max_iter', type=int, nargs='?', default=15, help='最大迭代次数 (默认: 15)')
    parser.add_argument('--ucb', action='store_true', help='启用UCB策略')
    parser.add_argument('--ucb-c', type=float, default=1.414, help='UCB探索参数 (默认: 1.414)')
    parser.add_argument('--ucb-mode', type=str, default='standard', choices=['standard', 'tuned'],
                        help='UCB模式 (默认: standard)')

    args = parser.parse_args()

    run_past_experiment(
        target_file=args.target,
        repetitions=args.repetitions,
        max_iter=args.max_iter,
        use_ucb=args.ucb,
        ucb_c=args.ucb_c,
        ucb_mode=args.ucb_mode
    )