# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b or b == c or a == c
# 重复次数: 2, 迭代: 7
# 生成时间: 2026-04-18 17:24:04

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入
    ("test", "test", "test", "ERROR"),
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 2, 0, "INVALID"),
    (1, 1, 3, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 等腰三角形
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 3, "ISOSCELES"),
    (4, 3, 3, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    # 边界条件
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    # 非整数/非浮点数输入
    ("1", 2, 3, "ERROR"),
    (1, "2", 3, "ERROR"),
    (1, 2, "3", "ERROR"),
    # 非法数值类型
    (None, 2, 3, "ERROR"),
    (True, 2, 3, "ERROR"),
    (False, 2, 3, "ERROR"),
    # 三角形不等式验证
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 10, "INVALID"),
    # 条件分支覆盖
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (2, 3, 4, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected