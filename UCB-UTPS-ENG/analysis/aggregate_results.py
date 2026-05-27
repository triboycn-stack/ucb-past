# analysis/aggregate_results.py
"""结果汇总和统计分析"""

import os
import glob
import json
import numpy as np
from scipy import stats
from typing import Dict, List


class ResultAggregator:
    def __init__(self, results_dir="results"):
        self.results_dir = results_dir
        self.all_results = {}
    
    def load_all_results(self, target_file: str):
        method_patterns = {
            'PAST': f"past_{target_file}_*.json",
            'No-Healing': f"no_healing_{target_file}_*.json",
            'Hypothesis': f"hypothesis_{target_file}_*.json",
            'SmartRandom': f"smartrandom_{target_file}_*.json",
            'Pure LLM': f"purellm_{target_file}_*.json"
        }
        
        for method, pattern in method_patterns.items():
            files = glob.glob(os.path.join(self.results_dir, pattern))
            if files:
                latest = max(files, key=os.path.getctime)
                with open(latest, 'r') as f:
                    self.all_results[method] = json.load(f)
                print(f"✅ 加载 {method}: {os.path.basename(latest)}")
        
        return self.all_results
    
    def compute_stats(self) -> Dict:
        stats = {}
        
        for method, data in self.all_results.items():
            stats[method] = {
                'effective_mean': np.mean(data['final_effective_coverage']),
                'effective_std': np.std(data['final_effective_coverage']),
                'effective_values': data['final_effective_coverage'],
                'line_mean': np.mean(data['final_line_coverage']),
                'line_std': np.std(data['final_line_coverage']),
                'branch_mean': np.mean(data['final_branch_coverage']),
                'branch_std': np.std(data['final_branch_coverage'])
            }
            
            # PAST和No-Healing特有
            if method in ['PAST', 'No-Healing']:
                if data.get('final_condition_path_coverage'):
                    stats[method]['condition_mean'] = np.mean(data['final_condition_path_coverage'])
                    stats[method]['condition_std'] = np.std(data['final_condition_path_coverage'])
                    stats[method]['condition_values'] = data['final_condition_path_coverage']
        
        return stats
    
    def run_wilcoxon_tests(self, stats: Dict) -> Dict:
        results = {}
        if 'PAST' not in stats:
            return results
        
        past_values = stats['PAST']['effective_values']
        
        for method in ['No-Healing', 'Hypothesis', 'SmartRandom', 'Pure LLM']:
            if method in stats:
                baseline = stats[method]['effective_values']
                if len(past_values) == len(baseline):
                    try:
                        _, p_value = stats.wilcoxon(past_values, baseline, alternative='two-sided')
                        effect = self._cliff_delta(past_values, baseline)
                        results[method] = {
                            'p_value': p_value,
                            'significant': p_value < 0.05,
                            'effect_size': effect,
                            'mean_past': np.mean(past_values),
                            'mean_baseline': np.mean(baseline),
                            'improvement': np.mean(past_values) - np.mean(baseline)
                        }
                    except:
                        pass
        return results
    
    def _cliff_delta(self, x, y):
        n_x, n_y = len(x), len(y)
        if n_x == 0 or n_y == 0:
            return 0.0
        delta = 0
        for xi in x:
            for yj in y:
                delta += 1 if xi > yj else (-1 if xi < yj else 0)
        return delta / (n_x * n_y)
    
    def print_table(self, stats: Dict, wilcoxon: Dict):
        print("\n" + "="*80)
        print("📊 实验结果汇总")
        print("="*80)
        
        # 表1: 条件路径覆盖（PAST/No-Healing）
        print("\n【表1: 条件路径覆盖率】(PAST主要指标)")
        print(f"{'方法':<20} {'条件路径覆盖率 (mean±std)':<30}")
        print("-"*50)
        for m in ['PAST', 'No-Healing']:
            if m in stats and 'condition_mean' in stats[m]:
                s = stats[m]
                print(f"{m:<20} {s['condition_mean']:>6.1f}% ± {s['condition_std']:<5.1f}%")
        
        # 表2: 有效行覆盖（统一指标）
        print("\n【表2: 有效行覆盖率】(统一比较指标)")
        print(f"{'方法':<20} {'有效行覆盖率 (mean±std)':<30}")
        print("-"*50)
        for m in ['PAST', 'No-Healing', 'Hypothesis', 'SmartRandom', 'Pure LLM']:
            if m in stats:
                s = stats[m]
                print(f"{m:<20} {s['effective_mean']:>6.1f}% ± {s['effective_std']:<5.1f}%")
        
        # 表3: Wilcoxon检验
        if wilcoxon:
            print("\n【表3: Wilcoxon检验】(PAST vs 其他 - 基于有效行覆盖)")
            print(f"{'对比方法':<20} {'p-value':<12} {'显著性':<10} {'效应量':<12}")
            print("-"*55)
            for m, w in wilcoxon.items():
                sig = "✅显著" if w['significant'] else "❌不显著"
                print(f"{m:<20} {w['p_value']:.4e}  {sig:<10} {w['effect_size']:>+.3f}")
        
        print("="*80)


def print_table(stats, wilcoxon):
    agg = ResultAggregator()
    agg.print_table(stats, wilcoxon)