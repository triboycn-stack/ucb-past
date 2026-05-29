# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b == c
# 重复次数: 3, 迭代: 12
# 生成时间: 2026-04-18 17:26:48

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形测试用例
    (3, 3, 3, "EQUILATERAL"),
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 5, "SCALENE"),
    # 无效三角形测试用例
    (1, 2, 3, "INVALID"),
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    # 输入错误测试用例
    ("a", 2, 3, "ERROR"),
    (1, "b", 3, "ERROR"),
    (1, 2, None, "ERROR"),
    # 边界条件测试用例
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    (1, 1, 1.9999999999, "ISOSCELES"),
    (1, 1, 2, "INVALID"),
    # 特殊情况测试用例
    (2, 2, 2, "EQUILATERAL"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 6, "ISOSCELES"),
    (5, 6, 7, "SCALENE"),
    (5, 5, 5.0, "EQUILATERAL"),
    (5.0, 5.0, 5.0, "EQUILATERAL"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected