# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b or b == c or a == c
# 重复次数: 3, 迭代: 4
# 生成时间: 2026-04-18 17:25:44

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证错误
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    (2, None, 3, "ERROR"),
    (2, 3, None, "ERROR"),
    # 非正数输入
    (-1, 2, 3, "INVALID"),
    (0, 2, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, -1, "INVALID"),
    (2, 3, 0, "INVALID"),
    # 无法构成三角形
    (1, 2, 3, "INVALID"),
    (2, 2, 5, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 不等边三角形
    (2, 3, 4, "SCALENE"),
    (3, 4, 5, "SCALENE"),
    (5, 12, 13, "SCALENE"),
    # 边界条件
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e-9, 1e-9, 1e-9 + 1e-18, "ISOSCELES"),
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    (1e9, 1e9, 1e9 + 1, "ISOSCELES"),
    # 异常情况
    (float('inf'), 1, 1, "INVALID"),
    (1, float('inf'), 1, "INVALID"),
    (1, 1, float('inf'), "INVALID"),
    (float('nan'), 1, 1, "ERROR"),
    (1, float('nan'), 1, "ERROR"),
    (1, 1, float('nan'), "ERROR"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected