# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b == c)
# 重复次数: 3, 迭代: 6
# 生成时间: 2026-04-18 17:26:02

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入：非数字类型
    ("test", "test", "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (3, None, 4, "ERROR"),
    (3, 4, None, "ERROR"),
    # 无效输入：负数或零
    (-1, 2, 3, "INVALID"),
    (0, 2, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, 2, -3, "INVALID"),
    (1, 2, 0, "INVALID"),
    # 无效输入：不满足三角形不等式
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
    # 边界条件：最小值
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    # 边界条件：最大值（假设为浮点数）
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 + 1, "ISOSCELES"),
    (1e10, 1e10 + 1, 1e10 + 2, "SCALENE"),
    # 非整数但有效
    (2.5, 2.5, 2.5, "EQUILATERAL"),
    (2.5, 2.5, 3.0, "ISOSCELES"),
    (2.5, 3.0, 4.0, "SCALENE"),
    # 浮点数边界情况
    (1.0, 1.0, 1.0, "EQUILATERAL"),
    (1.0, 1.0, 2.0, "INVALID"),
    (1.0, 2.0, 2.0, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected