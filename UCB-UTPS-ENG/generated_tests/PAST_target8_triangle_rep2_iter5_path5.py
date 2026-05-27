# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b or b == c or a == c
# 重复次数: 2, 迭代: 5
# 生成时间: 2026-04-26 06:54:17

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入
    ("test", "test", "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (1.0, "test", 3, "ERROR"),
    # 零或负数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 10, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 等腰三角形
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 3, "ISOSCELES"),
    (4, 3, 3, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    # 边界条件
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e-9, 1e-9, 1e-9 + 1e-10, "ISOSCELES"),
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    # 特殊情况：a == b == c（覆盖条件分支）
    (5, 5, 5, "EQUILATERAL"),
    # a == b
    (5, 5, 6, "ISOSCELES"),
    # b == c
    (5, 6, 6, "ISOSCELES"),
    # a == c
    (5, 6, 5, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected