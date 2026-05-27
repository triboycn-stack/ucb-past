# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or (not isinstance(c, (int, float)))
# 重复次数: 4, 迭代: 13
# 生成时间: 2026-04-18 17:30:32

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
    # 边界条件
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    (1, 1, 1.9999999999, "ISOSCELES"),
    (1, 1.0000000001, 1, "ISOSCELES"),
    # 非数值类型混合
    ("a", 2, 3, "ERROR"),
    (2, "b", 3, "ERROR"),
    (2, 3, "c", "ERROR"),
    # 非数值类型组合
    ("a", "b", "c", "ERROR"),
    # 特殊浮点值
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