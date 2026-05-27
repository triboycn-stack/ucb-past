# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a + b <= c or a + c <= b or b + c <= a
# 重复次数: 0, 迭代: 0
# 生成时间: 2026-04-18 17:19:05

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    (2, None, 3, "ERROR"),
    (2, 3, None, "ERROR"),
    # 零或负数
    (0, 2, 3, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    (2, 3, -1, "INVALID"),
    # 三角形不等式定理
    (1, 2, 3, "INVALID"),
    (2, 3, 5, "INVALID"),
    (3, 4, 8, "INVALID"),
    (5, 5, 10, "INVALID"),
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
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    (1, 1, 1.9999999999, "ISOSCELES"),
    (1, 1.9999999999, 1, "ISOSCELES"),
    (1.9999999999, 1, 1, "ISOSCELES"),
    (1, 2, 2.9999999999, "ISOSCELES"),
    (1, 2.9999999999, 2, "ISOSCELES"),
    (2.9999999999, 1, 2, "ISOSCELES"),
    (1, 2, 2.9999999999, "ISOSCELES"),
    (1, 2.9999999999, 2, "ISOSCELES"),
    (2.9999999999, 1, 2, "ISOSCELES"),
    # 异常情况
    (float('inf'), 2, 3, "INVALID"),
    (2, float('inf'), 3, "INVALID"),
    (2, 3, float('inf'), "INVALID"),
    (float('nan'), 2, 3, "ERROR"),
    (2, float('nan'), 3, "ERROR"),
    (2, 3, float('nan'), "ERROR"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected