# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b or b == c or a == c
# 重复次数: 2, 迭代: 3
# 生成时间: 2026-04-18 17:23:32

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证错误
    ("test", "test", "test", "ERROR"),
    (None, 1, 2, "ERROR"),
    (1.0, "test", 3, "ERROR"),
    # 非正数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    # 三角形不等式不满足
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 11, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    # 边界条件
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1, 1, 1.0, "EQUILATERAL"),
    (1, 2, 2, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    # 特殊情况
    (1, 1, 1.0000000001, "SCALENE"),
    (1.0000000001, 1, 1, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected