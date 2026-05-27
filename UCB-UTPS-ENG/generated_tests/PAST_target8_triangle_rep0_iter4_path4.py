# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a <= 0 or b <= 0 or c <= 0
# 重复次数: 0, 迭代: 4
# 生成时间: 2026-04-26 06:51:01

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证错误
    ("test", 3, 4, "ERROR"),
    (3, "test", 4, "ERROR"),
    (3, 4, "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (3, None, 4, "ERROR"),
    (3, 4, None, "ERROR"),
    # 零或负数边长
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 2, "INVALID"),
    (1, -1, 2, "INVALID"),
    (1, 2, 0, "INVALID"),
    (1, 2, -1, "INVALID"),
    # 不满足三角形不等式
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
    # 边界情况：最小值
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    # 边界情况：最大值（浮点数）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    # 临界值：刚好满足三角形不等式
    (1, 1, 1.9999999999, "ISOSCELES"),
    (1, 1.9999999999, 1, "ISOSCELES"),
    (1.9999999999, 1, 1, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected