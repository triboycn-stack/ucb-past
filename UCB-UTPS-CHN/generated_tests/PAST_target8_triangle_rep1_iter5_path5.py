# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b or b == c or a == c
# 重复次数: 1, 迭代: 5
# 生成时间: 2026-04-26 06:52:35

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
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 5, "INVALID"),
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
    # 边界条件：最小值
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e-9, 1e-9, 1e-9 + 1e-10, "ISOSCELES"),
    # 边界条件：最大值
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 - 1, "ISOSCELES"),
    # 非整数输入
    (2.5, 2.5, 2.5, "EQUILATERAL"),
    (2.5, 2.5, 3.0, "ISOSCELES"),
    (2.5, 3.0, 4.0, "SCALENE"),
    # 混合类型输入（合法）
    (2, 2.0, 2, "EQUILATERAL"),
    (2, 3.0, 2, "ISOSCELES"),
    # 条件分支覆盖
    (1, 1, 2, "ISOSCELES"),
    (1, 2, 1, "ISOSCELES"),
    (2, 1, 1, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    (2, 2, 3, "ISOSCELES"),
    (3, 3, 3, "EQUILATERAL"),
    (4, 5, 6, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected