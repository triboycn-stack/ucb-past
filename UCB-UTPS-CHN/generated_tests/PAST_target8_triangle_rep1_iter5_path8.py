# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b == c
# 重复次数: 1, 迭代: 5
# 生成时间: 2026-04-18 17:21:46

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 3, 3, "EQUILATERAL"),
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 5, "SCALENE"),
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
    (2, 3, 5, "INVALID"),
    (5, 5, 10, "INVALID"),
    # 输入错误（非数字）
    ("test", 2, 3, "ERROR"),
    (1, "test", 3, "ERROR"),
    (1, 2, "test", "ERROR"),
    # 边界情况（最小值）
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1, 1, 1, "EQUILATERAL"),
    # 边界情况（最大值）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    (1e100, 1e100, 1e100 + 1, "SCALENE"),
    # 等腰三角形（不同边组合）
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 不等边三角形
    (2, 3, 4, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    # 非法输入（字符串）
    ("a", "b", "c", "ERROR"),
    # 非法输入（None）
    (None, 1, 2, "ERROR"),
    (1, None, 2, "ERROR"),
    (1, 2, None, "ERROR"),
    # 非法输入（布尔值）
    (True, 1, 2, "ERROR"),
    (1, True, 2, "ERROR"),
    (1, 2, True, "ERROR"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected