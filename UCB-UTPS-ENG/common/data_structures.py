# common/data_structures.py
"""数据结构定义"""

from dataclasses import dataclass, field
from typing import List, Optional
import json
from datetime import datetime


@dataclass
class ExperimentResult:
    """实验结果数据结构"""
    method_name: str
    target_file: str
    repetitions: int
    max_iter: int
    timestamp: str
    
    # PAST和No-Healing的主要指标
    condition_path_coverage_history: Optional[List[List[float]]] = None
    final_condition_path_coverage: Optional[List[float]] = None
    
    # 所有方法的统一比较指标（有效行覆盖）
    effective_line_coverage_history: Optional[List[List[float]]] = None
    final_effective_coverage: Optional[List[float]] = None
    
    # 参考指标
    line_coverage_history: Optional[List[List[float]]] = None
    branch_coverage_history: Optional[List[List[float]]] = None
    final_line_coverage: Optional[List[float]] = None
    final_branch_coverage: Optional[List[float]] = None
    
    def save(self, filename: str):
        """保存结果到JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    def to_dict(self) -> dict:
        return {
            'method_name': self.method_name,
            'target_file': self.target_file,
            'repetitions': self.repetitions,
            'max_iter': self.max_iter,
            'timestamp': self.timestamp,
            'condition_path_coverage_history': self.condition_path_coverage_history,
            'final_condition_path_coverage': self.final_condition_path_coverage,
            'effective_line_coverage_history': self.effective_line_coverage_history,
            'final_effective_coverage': self.final_effective_coverage,
            'line_coverage_history': self.line_coverage_history,
            'branch_coverage_history': self.branch_coverage_history,
            'final_line_coverage': self.final_line_coverage,
            'final_branch_coverage': self.final_branch_coverage
        }
    
    @classmethod
    def load(cls, filename: str):
        """从JSON加载结果"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return cls(**data)