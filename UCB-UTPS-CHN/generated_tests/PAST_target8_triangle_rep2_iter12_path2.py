# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a + b <= c or a + c <= b or b + c <= a
# 重复次数: 2, 迭代: 12
# 生成时间: 2026-04-18 17:24:48

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证
    ("test", 3, 4, "ERROR"),
    (3, "test", 4, "ERROR"),
    (3, 4, "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (3, None, 4, "ERROR"),
    (3, 4, None, "ERROR"),
    (True, 3, 4, "ERROR"),
    (3, True, 4, "ERROR"),
    (3, 4, True, "ERROR"),
    (1.1, 2.2, 3.3, "SCALENE"),
    
    # 非正数输入
    (-1, 2, 3, "INVALID"),
    (0, 2, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, 2, -3, "INVALID"),
    (1, 2, 0, "INVALID"),
    
    # 三角形不等式定理
    (1, 2, 3, "INVALID"),
    (2, 3, 5, "INVALID"),
    (3, 4, 8, "INVALID"),
    (1, 1, 2, "INVALID"),
    (2, 2, 5, "INVALID"),
    (3, 3, 7, "INVALID"),
    
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (3.0, 3.0, 3.0, "EQUILATERAL"),
    
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (3.0, 3.0, 4.0, "ISOSCELES"),
    (5, 5, 5.0, "EQUILATERAL"),
    
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
    (1, 2, 3.5, "SCALENE"),
    
    # 边界条件
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    (1, 1, 1.9999999999, "ISOSCELES"),
    (1, 1, 2, "INVALID"),
    (1, 1, 1.9999999999999999, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected