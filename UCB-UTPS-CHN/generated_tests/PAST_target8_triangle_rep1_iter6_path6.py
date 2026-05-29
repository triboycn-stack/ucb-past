# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a <= 0 or b <= 0 or c <= 0)
# 重复次数: 1, 迭代: 6
# 生成时间: 2026-04-26 06:52:43

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 4, 5, "SCALENE"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 3, "ISOSCELES"),
    (5, 4, 5, "ISOSCELES"),
    (4, 5, 5, "ISOSCELES"),
    
    # 无效三角形（边长为0或负数）
    (0, 4, 5, "INVALID"),
    (-1, 4, 5, "INVALID"),
    (3, 0, 5, "INVALID"),
    (3, -2, 5, "INVALID"),
    (3, 4, 0, "INVALID"),
    (3, 4, -1, "INVALID"),
    
    # 不满足三角形不等式定理
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    
    # 输入错误（非数字类型）
    ("test", 4, 5, "ERROR"),
    (3, "test", 5, "ERROR"),
    (3, 4, "test", "ERROR"),
    (None, 4, 5, "ERROR"),
    (3, None, 5, "ERROR"),
    (3, 4, None, "ERROR"),
    
    # 边界条件
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1, 1, 1.9999999999, "ISOSCELES"),
    (1, 1, 2, "INVALID"),
    (1, 1, 1.9999999999999999, "ISOSCELES"),
    (1, 1, 2.0, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    (1, 1, 1, "EQUILATERAL"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected