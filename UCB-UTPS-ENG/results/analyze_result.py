#!/usr/bin/env python3
"""
Complete Experimental Results Analysis - Wilcoxon Test + Visualization
Analyzes PAST, PAST-UCB, No-Healing, Hypothesis, SmartRandom, PureLLM
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

# ========= Font Settings =========
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


# ========= Wilcoxon Test Class =========
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


# ========= Result Loader =========
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
        # ========== All 6 methods ==========
        self.all_methods = ["past", "past_ucb", "no_healing", "hypothesis", "smartrandom", "purellm"]
        self.method_labels = {
            "past": "PAST",
            "past_ucb": "PAST-UCB",
            "no_healing": "No-Healing",
            "hypothesis": "Hypothesis",
            "smartrandom": "SmartRandom",
            "purellm": "PureLLM"
        }
        # Method colors
        self.method_colors = {
            "past": "#1f77b4",
            "past_ucb": "#2E86AB",
            "no_healing": "#A23B72",
            "hypothesis": "#F18F01",
            "smartrandom": "#6A4E9B",
            "purellm": "#C73E1D"
        }

    def find_files(self):
        """Find all JSON files"""
        files = {}
        for target in self.targets:
            files[target] = {}
            for method in self.all_methods:
                pattern = f"{method}_{target}*.json"
                matches = glob.glob(os.path.join(self.data_dir, pattern))
                if matches:
                    latest = max(matches, key=os.path.getmtime)
                    files[target][method] = latest
                    print(f"  ✅ {target} - {method}: {os.path.basename(latest)}")
                else:
                    files[target][method] = None
                    print(f"  ⚠️ {target} - {method}: Not found")
        return files

    def load_result(self, filepath):
        if not filepath or not os.path.exists(filepath):
            return None
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"  ❌ Failed to load {filepath}: {e}")
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


# ========= Chart Generator =========
class ChartGenerator:
    @staticmethod
    def plot_bar_chart(summary, targets, method_labels, method_colors, timestamp):
        """Bar chart (6 methods)"""
        methods = ["past", "past_ucb", "no_healing", "hypothesis", "smartrandom", "purellm"]
        method_display = ["PAST", "PAST-UCB", "No-Healing", "Hypothesis", "SmartRandom", "PureLLM"]
        colors = [method_colors[m] for m in methods]

        x = np.arange(len(targets))
        width = 0.13

        fig, ax = plt.subplots(figsize=(16, 8))

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
        ax.set_title('Effective Line Coverage Comparison Across All Methods', fontsize=14)
        ax.set_xticks(x + width * 2.5)
        ax.set_xticklabels([t.replace('target', 'T') for t in targets], rotation=45, ha='right')
        ax.legend(loc='lower right', fontsize=9, ncol=2)
        ax.set_ylim(0, 105)
        ax.grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        filename = f"coverage_comparison_all_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"  ✅ Bar chart saved: {filename}")
        plt.close()

    @staticmethod
    def plot_ranking(summary, targets, method_labels, method_colors, timestamp):
        """Ranking chart (6 methods)"""
        methods = ["past", "past_ucb", "no_healing", "hypothesis", "smartrandom", "purellm"]
        method_display = ["PAST", "PAST-UCB", "No-Healing", "Hypothesis", "SmartRandom", "PureLLM"]
        colors = [method_colors[m] for m in methods]

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
        bars = ax.bar(method_display, avg_ranks, color=colors)

        for bar, rank in zip(bars, avg_ranks):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                    f'{rank:.1f}', ha='center', va='bottom', fontsize=10)

        ax.set_ylabel('Average Rank (1=best)', fontsize=12)
        ax.set_title('Average Rank of Each Method Across All Targets', fontsize=14)
        ax.set_ylim(0, len(methods) + 0.5)
        ax.grid(True, alpha=0.3, axis='y')
        ax.invert_yaxis()

        plt.tight_layout()
        filename = f"ranking_comparison_all_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"  ✅ Ranking chart saved: {filename}")
        plt.close()

    @staticmethod
    def plot_heatmap(comparisons, targets, method_labels, timestamp):
        """p-value heatmap (PAST-UCB vs all other methods)"""
        methods = ["past", "no_healing", "hypothesis", "smartrandom", "purellm"]
        method_display = ["PAST", "No-Healing", "Hypothesis", "SmartRandom", "PureLLM"]

        if not targets:
            print("  ⚠️ No valid data for heatmap")
            return

        p_values = np.zeros((len(targets), len(methods)))
        for i, target in enumerate(targets):
            for j, method in enumerate(methods):
                if target in comparisons and method in comparisons[target]:
                    p_values[i, j] = comparisons[target][method]["p_value"]
                else:
                    p_values[i, j] = 1.0

        fig, ax = plt.subplots(figsize=(12, 8))
        im = ax.imshow(p_values, cmap='RdYlGn_r', aspect='auto', vmin=0, vmax=0.1)

        ax.set_xticks(np.arange(len(methods)))
        ax.set_yticks(np.arange(len(targets)))
        ax.set_xticklabels(method_display, rotation=45, ha='right')
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
        filename = f"wilcoxon_heatmap_all_{timestamp}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"  ✅ Heatmap saved: {filename}")
        plt.close()


# ========= Main Program =========
def main():
    print("=" * 80)
    print("Complete Experimental Results Analysis - All 6 Methods")
    print("=" * 80)
    print(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Find files
    print("\nScanning result files...")
    loader = ResultLoader()
    files = loader.find_files()

    # Load data
    print("\nLoading experimental results...")
    results = {}
    for target in files:
        results[target] = {}
        for method in files[target]:
            if files[target][method]:
                data = loader.load_result(files[target][method])
                results[target][method] = data
            else:
                results[target][method] = None
    print("  ✅ Load complete")

    # Extract coverage values
    def get_values(target, method):
        data = results.get(target, {}).get(method)
        return loader.extract_final_effective_coverage(data)

    # Compute summary statistics
    print("\n" + "=" * 100)
    print("Experimental Results Summary - Based on Effective Line Coverage (All 6 Methods)")
    print("=" * 100)

    summary = {}
    for target in loader.targets:
        summary[target] = {}
        for method in loader.all_methods:
            values = get_values(target, method)
            if values:
                summary[target][method] = {
                    "mean": np.mean(values),
                    "std": np.std(values),
                    "values": values
                }

    # Print table
    header = f"{'Target':<20}"
    for method in loader.all_methods:
        header += f"{loader.method_labels[method]:<14}"
    print(header)
    print("-" * (20 + 14 * len(loader.all_methods)))
    for target in loader.targets:
        row = f"{target:<20}"
        for method in loader.all_methods:
            if method in summary[target]:
                s = summary[target][method]
                row += f"{s['mean']:.1f}±{s['std']:.1f}%{' ':<6}"
            else:
                row += f"{'N/A':<14}"
        print(row)

    # Wilcoxon test (PAST-UCB vs all other methods)
    print("\n" + "=" * 120)
    print("Wilcoxon Test Results (PAST-UCB vs Other Methods)")
    print("=" * 120)

    comparisons = {}
    for target in loader.targets:
        target_values = get_values(target, "past_ucb")
        if not target_values:
            continue
        comparisons[target] = {}
        for method in ["past", "no_healing", "hypothesis", "smartrandom", "purellm"]:
            baseline_values = get_values(target, method)
            if not baseline_values:
                continue
            result = WilcoxonAnalyzer.compare(target_values, baseline_values)
            comparisons[target][method] = result

    # Print Wilcoxon table
    print(f"{'Target':<20} {'Method':<15} {'p-value':<12} {'Significant':<10} {'Effect Size':<12} {'PAST-UCB Mean':<14} {'Method Mean':<12} {'Improvement':<10}")
    print("-" * 115)
    for target in loader.targets:
        if target not in comparisons:
            continue
        target_vals = get_values(target, "past_ucb")
        mean_target = np.mean(target_vals) if target_vals else 0
        for method in ["past", "no_healing", "hypothesis", "smartrandom", "purellm"]:
            if method in comparisons[target]:
                r = comparisons[target][method]
                sig_mark = "✅Yes" if r['significant'] else "❌No"
                imp_sign = "+" if r['improvement'] > 0 else ""
                print(f"{target:<20} {loader.method_labels[method]:<15} "
                      f"{r['p_value']:.4e}  {sig_mark:<8} "
                      f"{r['effect_size']:+.3f}({r['effect_interpretation']:<8}) "
                      f"{r['mean_target']:>6.1f}%     {r['mean_baseline']:>6.1f}%     "
                      f"{imp_sign}{r['improvement']:>+6.1f}%")
    print("=" * 120)

    # Generate charts
    print("\n" + "=" * 80)
    print("Generating comparison charts")
    print("=" * 80)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    ChartGenerator.plot_bar_chart(summary, loader.targets, loader.method_labels, loader.method_colors, timestamp)
    ChartGenerator.plot_ranking(summary, loader.targets, loader.method_labels, loader.method_colors, timestamp)
    ChartGenerator.plot_heatmap(comparisons, list(comparisons.keys()), loader.method_labels, timestamp)

    # Save JSON results
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

    json_file = f"analysis_results_all_{timestamp}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n Analysis results saved: {json_file}")

    print("\n" + "=" * 80)
    print(" Analysis Complete!")
    print(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)


if __name__ == "__main__":
    main()