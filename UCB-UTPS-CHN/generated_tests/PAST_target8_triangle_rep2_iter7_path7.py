# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b or b == c or a == c)
# 重复次数: 2, 迭代: 7
# 生成时间: 2026-04-26 06:54:34

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入
    ("test", "test", "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (1, "test", 3, "ERROR"),
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 2, "INVALID"),
    (1, 2, 0, "INVALID"),
    (1, 1, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
    # 边界条件
    (1, 1, 1.999, "ISOSCELES"),
    (1, 1, 2, "INVALID"),
    (1, 1, 1.9999999999999999, "ISOSCELES"),
    (1e-10, 1e-10, 1e-10, "EQUILATERAL"),
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    # 特殊情况
    (1, 2, 2, "ISOSCELES"),
    (2, 2, 2, "EQUILATERAL"),
    (3, 4, 4, "ISOSCELES"),
    (4, 5, 5, "ISOSCELES"),
    (5, 5, 6, "ISOSCELES"),
    (5, 6, 6, "ISOSCELES"),
    (6, 6, 6, "EQUILATERAL"),
    (7, 8, 9, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected