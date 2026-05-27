#!/usr/bin/env python3
"""
实验结果分析程序 - Wilcoxon检验 + 可视化
分析 PAST-UCB vs No-Healing、Hypothesis、SmartRandom、PureLLM
输出 JSON 汇总文件 + 图表
"""

import os
import json
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from scipy import stats
from typing import Dict, List
from datetime import datetime

# ========= 中文字体设置 =========
try:
    font_list = [f.name for f in fm.fontManager.ttflist if
                 any(k in f.name for k in ['SimHei', 'Microsoft YaHei', 'Noto Sans CJK SC'])]
    if font_list:
        plt.rcParams['font.sans-serif'] = font_list[0]
    else:
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
except:
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False


# ========= Wilcoxon 检验类 =========
class WilcoxonAnalyzer:
    @staticmethod
    def compare(target_scores: List[float], baseline_scores: List[float]) -> Dict:
        if len(target_scores) != len(baseline_scores):
            min_len = min(len(target_scores), len(baseline_scores))
            target_scores = target_scores[:min_len]
            baseline_scores = baseline_scores[:min_len]

        if len(target_scores) < 2:
            return {
                "p_value": 1.0,
                "significant": False,
                "effect_size": 0.0,
                "effect_interpretation": "insufficient_data",
                "mean_target": np.mean(target_scores) if target_scores else 0,
                "mean_baseline": np.mean(baseline_scores) if baseline_scores else 0,
                "improvement": 0.0
            }

        try:
            statistic, p_value = stats.wilcoxon(target_scores, baseline_scores, alternative='two-sided')
        except:
            statistic, p_value = stats.mannwhitneyu(target_scores, baseline_scores, alternative='two-sided')

        def cliff_delta(x, y):
            n_x = len(x)
            n_y = len(y)
            if n_x == 0 or n_y == 0:
                return 0.0
            delta = 0
            for xi in x:
                for yj in y:
                    if xi > yj:
                        delta += 1
                    elif xi < yj:
                        delta -= 1
            return delta / (n_x * n_y)

        effect_size = cliff_delta(target_scores, baseline_scores)

        if abs(effect_size) < 0.147:
            effect_interpretation = "negligible"
        elif abs(effect_size) < 0.33:
            effect_interpretation = "small"
        elif abs(effect_size) < 0.474:
            effect_interpretation = "medium"
        else:
            effect_interpretation = "large"

        significant = p_value < 0.05

        return {
            "p_value": p_value,
            "significant": significant,
            "effect_size": effect_size,
            "effect_interpretation": effect_interpretation,
            "mean_target": float(np.mean(target_scores)),
            "mean_baseline": float(np.mean(baseline_scores)),
            "improvement": float(np.mean(target_scores) - np.mean(baseline_scores))
        }


# ========= 结果加载器 =========
class ResultLoader:
    def __init__(self, data_dir="."):
        self.data_dir = data_dir
        self.targets = [
            "target4_dedent",
            "target5_scanstring",
            "target6_statemachine",
            "target7_closure",
            "target8_triangle",
            "target9_nextdate",
            "target10_commission"
        ]
        self.target_method = "past_ucb"
        self.baseline_methods = ["no_healing", "hypothesis", "smartrandom", "purellm"]
        self.method_labels = {
            "past_ucb": "PAST-UCB",
            "no_healing": "No-Healing",
            "hypothesis": "Hypothesis",
            "smartrandom": "SmartRandom",
            "purellm": "PureLLM"
        }

    def find_files(self):
        files = {}
        for target in self.targets:
            files[target] = {}

            # PAST-UCB
            ucb_pattern = f"past_ucb_{target}*.json"
            ucb_matches = glob.glob(os.path.join(self.data_dir, ucb_pattern))
            if ucb_matches:
                files[target][self.target_method] = max(ucb_matches, key=os.path.getmtime)
                print(f"  ✅ {target} - PAST-UCB: {os.path.basename(files[target][self.target_method])}")
            else:
                files[target][self.target_method] = None
                print(f"  ⚠️ {target} - PAST-UCB: 未找到")

            # 基线方法
            for method in self.baseline_methods:
                pattern = f"{method}_{target}*.json"
                matches = glob.glob(os.path.join(self.data_dir, pattern))
                if matches:
                    files[target][method] = max(matches, key=os.path.getmtime)
                    print(f"  ✅ {target} - {method}: {os.path.basename(files[target][method])}")
                else:
                    files[target][method] = None
                    print(f"  ⚠️ {target} - {method}: 未找到")
        return files

    def load_result(self, filepath):
        if not filepath or not os.path.exists(filepath):
            return None
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"  ❌ 加载失败 {filepath}: {e}")
            return None

    def extract_final_effective_coverage(self, data):
        if data is None:
            return []
        if 'final_effective_coverage' in data:
            values = data['final_effective_coverage']
            return values if isinstance(values, list) else [values]
        elif 'effective_line_coverage_history' in data and data['effective_line_coverage_history']:
            return [history[-1] for history in data['effective_line_coverage_history'] if history]
        elif 'final_line_coverage' in data:
            values = data['final_line_coverage']
            return values if isinstance(values, list) else [values]
        else:
            return []


# ========= 图表绘制类 =========
class ChartGenerator:
    @staticmethod
    def plot_bar_chart(summary, targets, method_labels, colors, timestamp):
        """柱状图"""
        methods = ["past_ucb", "no_healing", "hypothesis", "smartrandom", "purellm"]
        method_display = ["PAST-UCB", "No-Healing", "Hypothesis", "SmartRandom", "PureLLM"]

        x = np.arange(len(targets))
        width = 0.15

        fig, ax = plt.subplots(figsize=(14, 8))

        for i, (method, label, color) in enumerate(zip(methods, method_display, colors)):
            means = []
            stds = []
            for target in targets:
                if method in summary[target] and summary[target][method]:
                    means.append(summary[target][method]["mean"])
                    stds.append(summary[target][method]["std"])
                else:
                    means.append(0)
                    stds.append(0)
            ax.bar(x + i * width, means, width, label=label, color=color, yerr=stds,
                   capsize=3, error_kw={'linewidth': 1})

        ax.set_xlabel('Target Program', fontsize=12)
        ax.set_ylabel('Effective Line Coverage (%)', fontsize=12)
        ax.set_title('Effective Line Coverage Comparison Across Methods', fontsize=14)
        ax.set_xticks(x + width * 2)
        ax.set_xticklabels([t.replace('target', 'T') for t in targets], rotation=45, ha='right')
        ax.legend(loc='lower right', fontsize=10)
        ax.set_ylim(0, 105)
        ax.grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        filename = f"coverage_comparison_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"  ✅ 柱状图: {filename}")
        plt.close()

    @staticmethod
    def plot_heatmap(comparisons, targets, timestamp):
        """p-value热力图"""
        methods = ["no_healing", "hypothesis", "smartrandom", "purellm"]
        method_labels = ["No-Healing", "Hypothesis", "SmartRandom", "PureLLM"]

        if not targets:
            print("  ⚠️ 无有效数据生成热力图")
            return

        p_values = np.zeros((len(targets), len(methods)))
        for i, target in enumerate(targets):
            for j, method in enumerate(methods):
                if target in comparisons and method in comparisons[target]:
                    p_values[i, j] = comparisons[target][method]["p_value"]
                else:
                    p_values[i, j] = 1.0

        fig, ax = plt.subplots(figsize=(10, 8))
        im = ax.imshow(p_values, cmap='RdYlGn_r', aspect='auto', vmin=0, vmax=0.1)

        ax.set_xticks(np.arange(len(methods)))
        ax.set_yticks(np.arange(len(targets)))
        ax.set_xticklabels(method_labels, rotation=45, ha='right')
        ax.set_yticklabels([t.replace('target', 'T') for t in targets])

        for i in range(len(targets)):
            for j in range(len(methods)):
                color = 'white' if p_values[i, j] < 0.05 else 'black'
                sig_mark = '*' if p_values[i, j] < 0.05 else ''
                text = f"{p_values[i, j]:.3f}{sig_mark}"
                ax.text(j, i, text, ha="center", va="center", color=color, fontsize=9)

        ax.set_title("Wilcoxon Test p-value (PAST-UCB vs Others)\n* indicates p<0.05", fontsize=14)
        plt.colorbar(im, ax=ax, label='p-value')

        plt.tight_layout()
        filename = f"wilcoxon_heatmap_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"  ✅ 热力图: {filename}")
        plt.close()

    @staticmethod
    def plot_effect_size(comparisons, targets, timestamp):
        """效应量对比图"""
        methods = ["no_healing", "hypothesis", "smartrandom", "purellm"]
        method_labels = ["No-Healing", "Hypothesis", "SmartRandom", "PureLLM"]
        colors = ['#A23B72', '#F18F01', '#6A4E9B', '#C73E1D']

        if not targets:
            print("  ⚠️ 无有效数据生成效应量图")
            return

        x = np.arange(len(targets))
        width = 0.2

        fig, ax = plt.subplots(figsize=(14, 8))

        for i, (method, label, color) in enumerate(zip(methods, method_labels, colors)):
            effect_sizes = []
            for target in targets:
                if target in comparisons and method in comparisons[target]:
                    effect_sizes.append(comparisons[target][method]["effect_size"])
                else:
                    effect_sizes.append(0)
            ax.bar(x + i * width, effect_sizes, width, label=label, color=color)

        ax.axhline(y=0.147, color='gray', linestyle='--', alpha=0.5, label='small (0.147)')
        ax.axhline(y=0.33, color='gray', linestyle='--', alpha=0.5, label='medium (0.33)')
        ax.axhline(y=0.474, color='gray', linestyle='--', alpha=0.5, label='large (0.474)')

        ax.set_xlabel('Target Program', fontsize=12)
        ax.set_ylabel("Cliff's Delta (Effect Size)", fontsize=12)
        ax.set_title("Effect Size: PAST-UCB vs Others\n(Positive means PAST-UCB is better)", fontsize=14)
        ax.set_xticks(x + width * 1.5)
        ax.set_xticklabels([t.replace('target', 'T') for t in targets], rotation=45, ha='right')
        ax.legend(loc='upper right', fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        filename = f"effect_size_comparison_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"  ✅ 效应量图: {filename}")
        plt.close()

    @staticmethod
    def plot_ranking(summary, targets, timestamp):
        """排名图"""
        methods = ["past_ucb", "no_healing", "hypothesis", "smartrandom", "purellm"]
        method_labels = ["PAST-UCB", "No-Healing", "Hypothesis", "SmartRandom", "PureLLM"]
        colors = ['#2E86AB', '#A23B72', '#F18F01', '#6A4E9B', '#C73E1D']

        if not targets:
            print("  ⚠️ 无有效数据生成排名图")
            return

        rankings = []
        for target in targets:
            scores = []
            for method in methods:
                if method in summary[target] and summary[target][method]:
                    scores.append(summary[target][method]["mean"])
                else:
                    scores.append(0)
            sorted_indices = np.argsort(scores)[::-1]
            rank_scores = [0] * len(scores)
            for rank, idx in enumerate(sorted_indices, 1):
                rank_scores[idx] = rank
            rankings.append(rank_scores)

        rankings = np.array(rankings)
        avg_ranks = np.mean(rankings, axis=0)

        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(method_labels, avg_ranks, color=colors)

        for bar, rank in zip(bars, avg_ranks):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                    f'{rank:.1f}', ha='center', va='bottom', fontsize=10)

        ax.set_ylabel('Average Rank (1=best)', fontsize=12)
        ax.set_title('Average Rank of Each Method Across All Targets', fontsize=14)
        ax.set_ylim(0, len(methods) + 0.5)
        ax.grid(True, alpha=0.3, axis='y')
        ax.invert_yaxis()

        plt.tight_layout()
        filename = f"ranking_comparison_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"  ✅ 排名图: {filename}")
        plt.close()


# ========= 主程序 =========
def main():
    print("=" * 80)
    print("🔬 实验结果分析 - PAST-UCB vs 基线方法")
    print("=" * 80)
    print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # 查找文件
    print("\n📁 扫描结果文件...")
    loader = ResultLoader()
    files = loader.find_files()

    # 加载数据
    print("\n📂 加载实验结果...")
    results = {}
    for target in files:
        results[target] = {}
        for method in files[target]:
            if files[target][method]:
                data = loader.load_result(files[target][method])
                results[target][method] = data
            else:
                results[target][method] = None
    print("  ✅ 加载完成")

    # 提取覆盖率值
    def get_values(target, method):
        data = results.get(target, {}).get(method)
        return loader.extract_final_effective_coverage(data)

    # 计算汇总统计
    print("\n" + "=" * 100)
    print("📊 实验结果汇总 - 基于有效行覆盖率")
    print("=" * 100)

    summary = {}
    for target in loader.targets:
        summary[target] = {}
        for method in ["past_ucb", "no_healing", "hypothesis", "smartrandom", "purellm"]:
            values = get_values(target, method)
            if values:
                summary[target][method] = {
                    "mean": np.mean(values),
                    "std": np.std(values),
                    "values": values
                }

    # 打印表格
    header = f"{'目标文件':<25} {'PAST-UCB':<18} {'No-Healing':<18} {'Hypothesis':<18} {'SmartRandom':<18} {'PureLLM':<18}"
    print(header)
    print("-" * (25 + 18 * 5))
    for target in loader.targets:
        row = f"{target:<25}"
        for method in ["past_ucb", "no_healing", "hypothesis", "smartrandom", "purellm"]:
            if method in summary[target]:
                s = summary[target][method]
                row += f"{s['mean']:.1f}% ± {s['std']:.1f}%{' ':<4}"
            else:
                row += f"{'N/A':<18}"
        print(row)

    # Wilcoxon检验
    print("\n" + "=" * 120)
    print("📊 Wilcoxon 统计检验结果 (PAST-UCB vs 其他方法)")
    print("=" * 120)

    comparisons = {}
    for target in loader.targets:
        target_values = get_values(target, "past_ucb")
        if not target_values:
            continue
        comparisons[target] = {}
        for method in ["no_healing", "hypothesis", "smartrandom", "purellm"]:
            baseline_values = get_values(target, method)
            if not baseline_values:
                continue
            result = WilcoxonAnalyzer.compare(target_values, baseline_values)
            comparisons[target][method] = result

    # 打印Wilcoxon表格
    print(
        f"{'目标文件':<20} {'对比方法':<15} {'p-value':<12} {'显著性':<10} {'效应量':<12} {'PAST-UCB均值':<14} {'方法均值':<12} {'提升':<10}")
    print("-" * 115)
    for target in loader.targets:
        if target not in comparisons:
            continue
        target_vals = get_values(target, "past_ucb")
        mean_target = np.mean(target_vals) if target_vals else 0
        for method in ["no_healing", "hypothesis", "smartrandom", "purellm"]:
            if method in comparisons[target]:
                r = comparisons[target][method]
                sig_mark = "✅显著" if r['significant'] else "❌不显著"
                imp_sign = "+" if r['improvement'] > 0 else ""
                print(f"{target:<20} {loader.method_labels[method]:<15} "
                      f"{r['p_value']:.4e}  {sig_mark:<8} "
                      f"{r['effect_size']:+.3f}({r['effect_interpretation']:<8}) "
                      f"{r['mean_target']:>6.1f}%     {r['mean_baseline']:>6.1f}%     "
                      f"{imp_sign}{r['improvement']:>+6.1f}%")
    print("=" * 120)

    # 优势分析
    print("\n" + "=" * 80)
    print("📊 PAST-UCB 优势分析")
    print("=" * 80)

    all_comps = []
    for target in comparisons:
        mean_target = np.mean(get_values(target, "past_ucb"))
        for method, r in comparisons[target].items():
            all_comps.append({
                "target": target,
                "method": method,
                "improvement": r['improvement'],
                "mean_target": mean_target,
                "mean_baseline": r['mean_baseline']
            })

    all_comps.sort(key=lambda x: x['improvement'], reverse=True)
    print("\n🏆 PAST-UCB 优势最大的对比 (提升幅度):")
    for i, comp in enumerate(all_comps[:5], 1):
        print(f"  {i}. {comp['target']} vs {loader.method_labels[comp['method']]}: "
              f"{comp['mean_target']:.1f}% vs {comp['mean_baseline']:.1f}% (+{comp['improvement']:.1f}%)")

    all_comps.sort(key=lambda x: x['improvement'])
    print("\n⚠️ PAST-UCB 劣势最大的对比 (下降幅度):")
    for i, comp in enumerate(all_comps[:3], 1):
        if comp['improvement'] >= 0:
            break
        print(f"  {i}. {comp['target']} vs {loader.method_labels[comp['method']]}: "
              f"{comp['mean_target']:.1f}% vs {comp['mean_baseline']:.1f}% ({comp['improvement']:.1f}%)")

    # 生成图表
    print("\n" + "=" * 80)
    print("📊 生成对比图表")
    print("=" * 80)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#6A4E9B', '#C73E1D']

    ChartGenerator.plot_bar_chart(summary, loader.targets, loader.method_labels, colors, timestamp)
    ChartGenerator.plot_heatmap(comparisons, list(comparisons.keys()), timestamp)
    ChartGenerator.plot_effect_size(comparisons, list(comparisons.keys()), timestamp)
    ChartGenerator.plot_ranking(summary, loader.targets, timestamp)

    # 保存JSON结果（与你之前的格式一致）
    output = {
        "timestamp": timestamp,
        "target_method": "PAST-UCB",
        "summary": {},
        "wilcoxon_tests": comparisons
    }

    for target in summary:
        output["summary"][target] = {}
        for method in summary[target]:
            output["summary"][target][method] = {
                "mean": summary[target][method]["mean"],
                "std": summary[target][method]["std"],
                "values": summary[target][method]["values"]
            }

    json_file = f"analysis_results_{timestamp}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n💾 分析结果已保存: {json_file}")

    print("\n" + "=" * 80)
    print("✨ 分析完成!")
    print(f"结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)


if __name__ == "__main__":
    main()