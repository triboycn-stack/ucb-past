# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a + b <= c or a + c <= b or b + c <= a)
# 重复次数: 4, 迭代: 12
# 生成时间: 2026-04-18 17:29:29

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 4, 5, "SCALENE"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 3, "ISOSCELES"),
    (2, 2, 3, "ISOSCELES"),
    (7, 8, 9, "SCALENE"),
    # 无效三角形（边长不符合）
    (1, 2, 3, "INVALID"),
    (2, 2, 5, "INVALID"),
    (1, 1, 100, "INVALID"),
    # 输入验证（非数字）
    ("test", 2, 3, "ERROR"),
    (1, "test", 3, "ERROR"),
    (1, 2, "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    (1, None, 3, "ERROR"),
    (1, 2, None, "ERROR"),
    # 零或负数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    # 边界条件
    (1e-10, 1e-10, 1e-10, "EQUILATERAL"),
    (1e-10, 1e-10, 1e-9, "ISOSCELES"),
    (1e-10, 1e-9, 1e-9, "ISOSCELES"),
    (1e-10, 1e-10, 1e-10 + 1e-10, "SCALENE"),
    # 特殊情况
    (1, 1, 1, "EQUILATERAL"),
    (2, 3, 2, "ISOSCELES"),
    (3, 4, 4, "ISOSCELES"),
    (4, 5, 6, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected