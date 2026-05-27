# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b == c)
# 重复次数: 4, 迭代: 9
# 生成时间: 2026-04-26 06:57:40

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 4, 5, "SCALENE"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 6, "ISOSCELES"),
    (2, 2, 3, "ISOSCELES"),
    (7, 8, 9, "SCALENE"),
    # 无效三角形（边长为0）
    (0, 4, 5, "INVALID"),
    (4, 0, 5, "INVALID"),
    (4, 5, 0, "INVALID"),
    # 无效三角形（边长为负数）
    (-1, 4, 5, "INVALID"),
    (4, -1, 5, "INVALID"),
    (4, 5, -1, "INVALID"),
    # 无效三角形（不满足三角形不等式）
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 输入错误（非数字类型）
    ("test", 4, 5, "ERROR"),
    (4, "test", 5, "ERROR"),
    (4, 5, "test", "ERROR"),
    (None, 4, 5, "ERROR"),
    (4, None, 5, "ERROR"),
    (4, 5, None, "ERROR"),
    # 边界情况（最小值）
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    # 边界情况（极大值）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    (1e100, 1e100, 1e100 + 1, "ISOSCELES"),
    # 条件分支覆盖（not (a == b == c)）
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 4, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected