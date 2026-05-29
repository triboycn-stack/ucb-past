# common/coverage_analyzer.py
"""有效行覆盖率分析器"""

import ast
import os


class CoverageAnalyzer:
    """有效行覆盖率分析器 - 排除死代码"""

    def __init__(self, source_file: str):
        self.source_file = source_file
        self.source = open(source_file, encoding='utf-8').read()
        self.lines = self.source.splitlines()
        self.effective_lines = self._compute_effective_lines()

        print(f"  [INFO] 有效行分析完成: 总行数={len(self.lines)}, 有效行数={len(self.effective_lines)}")

    def _compute_effective_lines(self) -> set:
        """计算有效行（排除静态分析确定的不可达代码）"""
        try:
            tree = ast.parse(self.source)
        except SyntaxError:
            # 如果解析失败，返回所有行
            return set(range(1, len(self.lines) + 1))

        all_lines = set(range(1, len(self.lines) + 1))
        dead_lines = self._identify_dead_code(tree)

        return all_lines - dead_lines

    def _identify_dead_code(self, tree: ast.AST) -> set:
        """识别死代码"""
        dead_lines = set()

        for node in ast.walk(tree):
            # 检查永远为假的条件分支
            if isinstance(node, ast.If):
                if self._is_always_false(node.test):
                    # if条件永远为假，那么if块内的代码是死代码
                    dead_lines.update(self._get_lines_in_block(node.body))
                elif self._is_always_true(node.test):
                    # if条件永远为真，那么else块内的代码是死代码
                    if node.orelse:
                        dead_lines.update(self._get_lines_in_block(node.orelse))

        return dead_lines

    def _is_always_false(self, test) -> bool:
        """判断条件是否永远为假"""
        if isinstance(test, ast.Constant):
            return not bool(test.value)
        return False

    def _is_always_true(self, test) -> bool:
        """判断条件是否永远为真"""
        if isinstance(test, ast.Constant):
            return bool(test.value)
        return False

    def _get_lines_in_block(self, block) -> set:
        """获取代码块中的所有行号"""
        lines = set()
        for stmt in block:
            if hasattr(stmt, 'lineno'):
                lines.add(stmt.lineno)
            # 递归获取子语句的行号
            for child in ast.walk(stmt):
                if hasattr(child, 'lineno'):
                    lines.add(child.lineno)
        return lines

    def compute_effective_coverage(self, covered_lines: set) -> float:
        """计算有效行覆盖率

        参数:
            covered_lines: 测试覆盖的行号集合

        返回:
            有效行覆盖率百分比
        """
        if not self.effective_lines:
            return 0.0

        # 计算覆盖的有效行
        effective_covered = covered_lines & self.effective_lines

        # 计算百分比
        result = len(effective_covered) / len(self.effective_lines) * 100

        # 调试输出
        print(
            f"        [DEBUG] 有效覆盖率计算: 覆盖行数={len(covered_lines)}, 有效行数={len(self.effective_lines)}, 有效覆盖行数={len(effective_covered)}, 结果={result:.1f}%")

        return result

    def get_effective_line_count(self) -> int:
        """获取有效行总数"""
        return len(self.effective_lines)