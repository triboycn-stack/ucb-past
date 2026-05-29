# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b or b == c or a == c)
# 重复次数: 3, 迭代: 3
# 生成时间: 2026-04-18 17:25:36

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入
    ("test", "test", "test", "ERROR"),
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 2, 0, "INVALID"),
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
    (1, 1, 1.9999999999, "ISOSCELES"),
    (1, 2, 2.9999999999, "ISOSCELES"),
    (1, 2, 3.0, "INVALID"),
    # 非数字输入
    ("a", 2, 3, "ERROR"),
    (1, "b", 3, "ERROR"),
    (1, 2, "c", "ERROR"),
    # 混合类型输入
    (1, 2, "3", "ERROR"),
    (1, "2", 3, "ERROR"),
    ("1", 2, 3, "ERROR"),
    # 特殊值
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