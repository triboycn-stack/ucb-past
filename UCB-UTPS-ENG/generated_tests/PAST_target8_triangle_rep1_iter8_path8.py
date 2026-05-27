# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b == c
# 重复次数: 1, 迭代: 8
# 生成时间: 2026-04-26 06:53:01

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 3, 3, "EQUILATERAL"),
    (2, 2, 3, "ISOSCELES"),
    (4, 5, 6, "SCALENE"),
    # 无效三角形（边长为0）
    (0, 1, 2, "INVALID"),
    (1, 0, 2, "INVALID"),
    (1, 2, 0, "INVALID"),
    # 无效三角形（负数）
    (-1, 2, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 2, -3, "INVALID"),
    # 无效三角形（不满足三角形不等式）
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 输入错误（非数字）
    ("test", 2, 3, "ERROR"),
    (1, "test", 3, "ERROR"),
    (1, 2, "test", "ERROR"),
    # 边界情况（最小值）
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "ISOSCELES"),
    (1, 2, 2, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    # 边界情况（最大值）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    (1e100, 1e100, 1e100 - 1, "ISOSCELES"),
    (1e100, 1e100 - 1, 1e100 - 1, "ISOSCELES"),
    (1e100, 1e100 - 1, 1e100 - 2, "SCALENE"),
    # 特殊情况（等腰但非等边）
    (2, 2, 2.0, "EQUILATERAL"),
    (2, 2, 3.0, "ISOSCELES"),
    (2, 3, 3.0, "ISOSCELES"),
    (3, 2, 2.0, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected