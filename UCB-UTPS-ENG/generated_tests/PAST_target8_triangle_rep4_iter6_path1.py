# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or (not isinstance(c, (int, float)))
# 重复次数: 4, 迭代: 6
# 生成时间: 2026-04-18 17:28:38

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
    # 非正数输入
    (-1, 2, 3, "INVALID"),
    (0, 2, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, 2, -3, "INVALID"),
    (1, 2, 0, "INVALID"),
    # 三角形不等式定理不满足
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (3.5, 3.5, 3.5, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (3.5, 3.5, 4, "ISOSCELES"),
    (3.5, 4, 3.5, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
    # 边界条件
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "ISOSCELES"),
    (1, 2, 2, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    (0.0001, 0.0001, 0.0001, "EQUILATERAL"),
    (1e-10, 1e-10, 1e-10, "EQUILATERAL"),
    (1e10, 1e10, 1e10, "EQUILATERAL"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected