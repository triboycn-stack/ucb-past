# analysis/plot_comparison.py
"""绘图比较"""

import matplotlib.pyplot as plt
import numpy as np


class ComparisonPlotter:
    def __init__(self, stats: dict, wilcoxon: dict):
        self.stats = stats
        self.wilcoxon = wilcoxon
        self.colors = {
            'PAST': '#2E86AB',
            'No-Healing': '#A23B72',
            'Hypothesis': '#F18F01',
            'SmartRandom': '#6A4E9B',
            'Pure LLM': '#C73E1D'
        }
    
    def plot_all(self, target_name: str):
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 图1: 最终有效行覆盖箱线图
        self._plot_boxplot(axes[0, 0], 'effective_values', '有效行覆盖率 (%)')
        
        # 图2: 收敛曲线
        self._plot_curves(axes[0, 1], 'effective_mean', '有效行覆盖率 (%)')
        
        # 图3: 条件路径覆盖（PAST vs No-Healing）
        self._plot_condition_path(axes[1, 0])
        
        # 图4: 效应量
        self._plot_effect_sizes(axes[1, 1])
        
        plt.suptitle(f"实验对比 - {target_name}", fontsize=14)
        plt.tight_layout()
        
        filename = f"comparison_{target_name}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"\n📊 保存: {filename}")
        plt.show()
    
    def _plot_boxplot(self, ax, key, ylabel):
        methods = list(self.stats.keys())
        data = [self.stats[m][key] for m in methods if key in self.stats[m]]
        bp = ax.boxplot(data, labels=methods, patch_artist=True)
        for patch, m in zip(bp['boxes'], methods):
            patch.set_facecolor(self.colors.get(m, '#999'))
        ax.set_ylabel(ylabel)
        ax.set_title('最终覆盖率对比')
        ax.grid(True, alpha=0.3)
    
    def _plot_curves(self, ax, key, ylabel):
        for m, s in self.stats.items():
            if key in s:
                mean = s[key]
                if isinstance(mean, np.ndarray) or len(mean) > 0:
                    x = range(1, len(mean) + 1)
                    ax.plot(x, mean, label=m, color=self.colors.get(m, '#000'), linewidth=2)
        ax.set_xlabel('迭代次数')
        ax.set_ylabel(ylabel)
        ax.set_title('收敛曲线')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_condition_path(self, ax):
        if 'PAST' in self.stats and 'No-Healing' in self.stats:
            if 'condition_values' in self.stats['PAST']:
                data = [self.stats['PAST']['condition_values'],
                       self.stats['No-Healing']['condition_values']]
                bp = ax.boxplot(data, labels=['PAST', 'No-Healing'], patch_artist=True)
                bp['boxes'][0].set_facecolor(self.colors['PAST'])
                bp['boxes'][1].set_facecolor(self.colors['No-Healing'])
                ax.set_ylabel('条件路径覆盖率 (%)')
                ax.set_title('条件路径覆盖对比')
                ax.grid(True, alpha=0.3)
    
    def _plot_effect_sizes(self, ax):
        if self.wilcoxon:
            methods = list(self.wilcoxon.keys())
            effects = [self.wilcoxon[m]['effect_size'] for m in methods]
            colors = ['red' if e < 0 else 'green' for e in effects]
            ax.bar(methods, effects, color=colors, alpha=0.7)
            ax.axhline(y=0, color='black', linewidth=0.5)
            ax.set_ylabel("Cliff's Delta")
            ax.set_title('效应量 (PAST vs 其他)')
            ax.grid(True, alpha=0.3)