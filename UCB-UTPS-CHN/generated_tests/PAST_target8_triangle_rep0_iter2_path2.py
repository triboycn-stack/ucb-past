# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a + b <= c or a + c <= b or b + c <= a
# 重复次数: 0, 迭代: 2
# 生成时间: 2026-04-26 06:50:42

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
    (2.5, "test", 3, "ERROR"),
    (2, 3.5, "test", "ERROR"),
    (2, "test", 3.5, "ERROR"),
    
    # 零或负数边长
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 2, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 2, 0, "INVALID"),
    (1, 2, -3, "INVALID"),
    
    # 三角形不等式定理
    (1, 1, 3, "INVALID"),
    (1, 3, 1, "INVALID"),
    (3, 1, 1, "INVALID"),
    (2, 2, 5, "INVALID"),
    (2, 5, 2, "INVALID"),
    (5, 2, 2, "INVALID"),
    (3, 4, 8, "INVALID"),
    (3, 8, 4, "INVALID"),
    (8, 3, 4, "INVALID"),
    
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (3.5, 3.5, 3.5, "EQUILATERAL"),
    
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (3.5, 3.5, 4, "ISOSCELES"),
    (3.5, 4, 3.5, "ISOSCELES"),
    (4, 3.5, 3.5, "ISOSCELES"),
    
    # 不等边三角形
    (2, 3, 4, "SCALENE"),
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected