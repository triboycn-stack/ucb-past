# common/wilcoxon_analyzer.py
"""Wilcoxon统计检验分析器"""

import numpy as np
from scipy import stats
from typing import List, Dict


class WilcoxonAnalyzer:
    """Wilcoxon符号秩检验分析器"""
    
    @staticmethod
    def compare(past_scores: List[float], baseline_scores: List[float],
                past_name: str = "PAST", baseline_name: str = "Baseline") -> Dict:
        """比较两组数据的显著性差异"""
        
        if len(past_scores) != len(baseline_scores):
            min_len = min(len(past_scores), len(baseline_scores))
            past_scores = past_scores[:min_len]
            baseline_scores = baseline_scores[:min_len]
        
        if len(past_scores) < 2:
            return {
                "p_value": 1.0,
                "significant": False,
                "effect_size": 0.0,
                "effect_interpretation": "insufficient_data",
                "mean_past": np.mean(past_scores) if past_scores else 0,
                "mean_baseline": np.mean(baseline_scores) if baseline_scores else 0,
                "improvement": 0.0
            }
        
        try:
            statistic, p_value = stats.wilcoxon(past_scores, baseline_scores, alternative='two-sided')
        except:
            statistic, p_value = stats.mannwhitneyu(past_scores, baseline_scores, alternative='two-sided')
        
        effect_size = WilcoxonAnalyzer._cliff_delta(past_scores, baseline_scores)
        
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
            "statistic": statistic,
            "p_value": p_value,
            "significant": significant,
            "effect_size": effect_size,
            "effect_interpretation": effect_interpretation,
            "mean_past": float(np.mean(past_scores)),
            "mean_baseline": float(np.mean(baseline_scores)),
            "improvement": float(np.mean(past_scores) - np.mean(baseline_scores))
        }
    
    @staticmethod
    def _cliff_delta(x: List[float], y: List[float]) -> float:
        """计算Cliff's Delta效应量"""
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
    
    @staticmethod
    def print_comparison(results: Dict, past_name: str = "PAST"):
        """打印比较结果"""
        print(f"\n{'='*80}")
        print(f"📊 Wilcoxon统计检验结果 ({past_name} vs 其他方法)")
        print(f"{'='*80}")
        print(f"{'对比方法':<20} {'PAST均值':<12} {'方法均值':<12} {'提升':<10} {'p-value':<12} {'显著性':<8} {'效应量':<10}")
        print("-"*90)
        
        for method, data in results.items():
            sig_mark = "✅显著" if data['significant'] else "❌不显著"
            improvement_sign = "+" if data['improvement'] > 0 else ""
            print(f"{method:<20} {data['mean_past']:>6.1f}%     {data['mean_baseline']:>6.1f}%     "
                  f"{improvement_sign}{data['improvement']:>+5.1f}%    {data['p_value']:.4e}  {sig_mark:<8} "
                  f"{data['effect_size']:>+.3f}")
        
        print("="*80)