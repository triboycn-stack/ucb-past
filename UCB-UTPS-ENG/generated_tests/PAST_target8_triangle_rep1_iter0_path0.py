# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or (not isinstance(c, (int, float))))
# 重复次数: 1, 迭代: 0
# 生成时间: 2026-04-26 06:51:53

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证
    ("test", "test", "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (1.0, "test", 3, "ERROR"),
    # 非正数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    # 三角形不等式定理
    (1, 2, 3, "INVALID"),
    (2, 3, 5, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (1.5, 1.5, 1.5, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (1.0, 1.0, 1.5, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
    # 边界条件
    (1, 1, 1.9999999999, "SCALENE"),
    (1, 1, 2, "INVALID"),
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e10, 1e10, 1e10, "EQUILATERAL"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected