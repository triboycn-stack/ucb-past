# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b == c
# 重复次数: 4, 迭代: 1
# 生成时间: 2026-04-18 17:27:57

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 3, 3, "EQUILATERAL"),
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 5, "SCALENE"),
    # 无效三角形
    (1, 2, 3, "INVALID"),
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    # 输入错误
    ("a", 2, 3, "ERROR"),
    (1, "b", 3, "ERROR"),
    (1, 2, None, "ERROR"),
    # 边界条件
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1, 1, 1.0, "EQUILATERAL"),
    (1, 2, 2, "ISOSCELES"),
    (2, 2, 3, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    (1, 1, 2, "INVALID"),
    # 特殊情况
    (1, 1, 1, "EQUILATERAL"),
    (2, 2, 2, "EQUILATERAL"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 6, "ISOSCELES"),
    (5, 6, 5, "ISOSCELES"),
    (6, 5, 5, "ISOSCELES"),
    (4, 5, 6, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected