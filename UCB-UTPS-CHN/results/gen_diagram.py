#根据analysis_results.json生成图表
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 读取正确的JSON数据
with open('analysis_results_20260517_090535.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

summary = data['summary']
wilcoxon = data['wilcoxon_tests']

# 目标列表（按顺序）
targets = ['target4_dedent', 'target5_scanstring', 'target6_statemachine',
           'target7_closure', 'target8_triangle', 'target9_nextdate', 'target10_commission']
target_labels = ['T4_dedent', 'T5_scanstring', 'T6_statemachine',
                 'T7_closure', 'T8_triangle', 'T9_nextdate', 'T10_commission']

# 方法列表
methods = ['past_ucb', 'no_healing', 'hypothesis', 'smartrandom', 'purellm']
method_labels = ['PAST-UCB', 'No-Healing', 'Hypothesis', 'SmartRandom', 'PureLLM']
method_colors = ['#2E86AB', '#A23B72', '#F18F01', '#6A4E9B', '#C73E1D']

# ========== 图1：柱状图 ==========
fig, ax = plt.subplots(figsize=(14, 8))
x = np.arange(len(targets))
width = 0.15

for i, (method, label, color) in enumerate(zip(methods, method_labels, method_colors)):
    means = []
    stds = []
    for target in targets:
        if method in summary[target]:
            means.append(summary[target][method]['mean'])
            stds.append(summary[target][method]['std'])
        else:
            means.append(0)
            stds.append(0)
    ax.bar(x + i * width, means, width, label=label, color=color,
           yerr=stds, capsize=3, error_kw={'linewidth': 1})

ax.set_xlabel('Target Program', fontsize=12)
ax.set_ylabel('Effective Line Coverage (%)', fontsize=12)
ax.set_title('Effective Line Coverage Comparison Across Methods', fontsize=14)
ax.set_xticks(x + width * 2)
ax.set_xticklabels(target_labels, rotation=45, ha='right')
ax.legend(loc='upper left', fontsize=10)
ax.set_ylim(0, 105)
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('coverage_comparison_correct.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ 图1已保存: coverage_comparison_correct.png")

# ========== 图2：热力图（p-value）==========
baseline_methods = ['no_healing', 'hypothesis', 'smartrandom', 'purellm']
baseline_labels = ['No-Healing', 'Hypothesis', 'SmartRandom', 'PureLLM']

p_values = np.zeros((len(targets), len(baseline_methods)))
for i, target in enumerate(targets):
    for j, method in enumerate(baseline_methods):
        if target in wilcoxon and method in wilcoxon[target]:
            p_values[i, j] = wilcoxon[target][method]['p_value']
        else:
            p_values[i, j] = 1.0

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(p_values, cmap='RdYlGn_r', aspect='auto', vmin=0, vmax=0.1)

ax.set_xticks(np.arange(len(baseline_methods)))
ax.set_yticks(np.arange(len(targets)))
ax.set_xticklabels(baseline_labels, rotation=45, ha='right')
ax.set_yticklabels(target_labels)

for i in range(len(targets)):
    for j in range(len(baseline_methods)):
        color = 'white' if p_values[i, j] < 0.05 else 'black'
        sig_mark = '*' if p_values[i, j] < 0.05 else ''
        text = f"{p_values[i, j]:.3f}{sig_mark}"
        ax.text(j, i, text, ha="center", va="center", color=color, fontsize=9)

ax.set_title("Wilcoxon Test p-value (PAST-UCB vs Others)\n* indicates p<0.05", fontsize=14)
plt.colorbar(im, ax=ax, label='p-value')
plt.tight_layout()
plt.savefig('wilcoxon_heatmap_correct.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ 图2已保存: wilcoxon_heatmap_correct.png")

# ========== 图3：效应量图 ==========
fig, ax = plt.subplots(figsize=(14, 8))
x = np.arange(len(targets))
width = 0.2

effect_colors = ['#A23B72', '#F18F01', '#6A4E9B', '#C73E1D']

for j, (method, label, color) in enumerate(zip(baseline_methods, baseline_labels, effect_colors)):
    effect_sizes = []
    for i, target in enumerate(targets):
        if target in wilcoxon and method in wilcoxon[target]:
            effect_sizes.append(wilcoxon[target][method]['effect_size'])
        else:
            effect_sizes.append(0)
    ax.bar(x + j * width, effect_sizes, width, label=label, color=color)

# 添加效应量阈值线
ax.axhline(y=0.147, color='gray', linestyle='--', alpha=0.5, label='small (0.147)')
ax.axhline(y=0.33, color='gray', linestyle='--', alpha=0.5, label='medium (0.33)')
ax.axhline(y=0.474, color='gray', linestyle='--', alpha=0.5, label='large (0.474)')

ax.set_xlabel('Target Program', fontsize=12)
ax.set_ylabel("Cliff's Delta (Effect Size)", fontsize=12)
ax.set_title("Effect Size: PAST-UCB vs Others\n(Positive means PAST-UCB is better)", fontsize=14)
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(target_labels, rotation=45, ha='right')
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')
ax.set_ylim(-1.1, 1.1)
plt.tight_layout()
plt.savefig('effect_size_comparison_correct.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ 图3已保存: effect_size_comparison_correct.png")

# ========== 图4：排名图 ==========
# 计算每个目标的排名
rankings = []
for target in targets:
    scores = []
    for method in methods:
        if method in summary[target]:
            scores.append(summary[target][method]['mean'])
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
bars = ax.bar(method_labels, avg_ranks, color=method_colors)

for bar, rank in zip(bars, avg_ranks):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            f'{rank:.1f}', ha='center', va='bottom', fontsize=10)

ax.set_ylabel('Average Rank (1=best)', fontsize=12)
ax.set_title('Average Rank of Each Method Across All Targets', fontsize=14)
ax.set_ylim(0, len(methods) + 0.5)
ax.grid(True, alpha=0.3, axis='y')
ax.invert_yaxis()
plt.tight_layout()
plt.savefig('ranking_comparison_correct.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ 图4已保存: ranking_comparison_correct.png")

print("\n所有图表已重新生成完成！")
print("文件列表：")
print("  - coverage_comparison_correct.png")
print("  - wilcoxon_heatmap_correct.png")
print("  - effect_size_comparison_correct.png")
print("  - ranking_comparison_correct.png")