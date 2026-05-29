# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a + b <= c or a + c <= b or b + c <= a
# 重复次数: 1, 迭代: 2
# 生成时间: 2026-04-26 06:52:10

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证
    ("test", "test", "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (1, "test", 3, "ERROR"),
    (1.0, 2, None, "ERROR"),
    
    # 非正数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 2, 0, "INVALID"),
    (1, 2, -3, "INVALID"),
    
    # 三角形不等式定理
    (1, 1, 3, "INVALID"),
    (1, 3, 1, "INVALID"),
    (3, 1, 1, "INVALID"),
    (2, 2, 5, "INVALID"),
    (5, 2, 2, "INVALID"),
    (2, 5, 2, "INVALID"),
    
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (5, 5, 6, "ISOSCELES"),
    (5, 6, 5, "ISOSCELES"),
    (6, 5, 5, "ISOSCELES"),
    
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    (2, 3, 4, "SCALENE"),
    (1, 2, 3, "INVALID"),  # 边界情况，不满足三角形不等式
    (1, 1, 1.999, "SCALENE"),  # 接近等边但不等
    (1, 1.0, 1.0, "EQUILATERAL"),  # 浮点与整数混合
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected