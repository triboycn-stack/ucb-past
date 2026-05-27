# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b or b == c or a == c)
# 重复次数: 4, 迭代: 7
# 生成时间: 2026-04-26 06:57:25

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入
    ("test", "test", "test", "ERROR"),
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, 2, 0, "INVALID"),
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 11, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (1.5, 1.5, 1.5, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (1.5, 1.5, 2, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2.1, 3.2, 4.3, "SCALENE"),
    # 边界情况
    (1, 1, 1.9999999999, "SCALENE"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    (1, 1, 1, "EQUILATERAL"),
    # 非数字输入
    ("a", 2, 3, "ERROR"),
    (1, "b", 3, "ERROR"),
    (1, 2, "c", "ERROR"),
    # 浮点数边界
    (1e-10, 1e-10, 1e-10, "EQUILATERAL"),
    (1e30, 1e30, 1e30, "EQUILATERAL"),
    # 条件分支覆盖
    (2, 3, 4, "SCALENE"),  # not (a == b or b == c or a == c)
    (2, 2, 3, "ISOSCELES"),  # a == b
    (2, 3, 3, "ISOSCELES"),  # b == c
    (3, 2, 2, "ISOSCELES"),  # a == c
    (2, 2, 2, "EQUILATERAL"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected