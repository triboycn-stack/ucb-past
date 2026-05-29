# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a <= 0 or b <= 0 or c <= 0)
# 重复次数: 2, 迭代: 6
# 生成时间: 2026-04-26 06:54:27

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 4, 5, "SCALENE"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 6, "ISOSCELES"),
    (2, 3, 4, "SCALENE"),
    (1, 1, 1, "EQUILATERAL"),
    (3, 4, 4, "ISOSCELES"),
    (5, 5, 5, "EQUILATERAL"),
    (7, 8, 9, "SCALENE"),
    (2, 2, 3, "ISOSCELES"),
    (10, 10, 10, "EQUILATERAL"),
    
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
    (5, 5, 11, "INVALID"),
    (1, 1, 3, "INVALID"),
    (2, 2, 5, "INVALID"),
    (3, 4, 8, "INVALID"),
    
    # 输入错误（非数字类型）
    ("a", 2, 3, "ERROR"),
    (1, "b", 3, "ERROR"),
    (1, 2, "c", "ERROR"),
    ("test", "test", "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    (True, 2, 3, "ERROR"),
    (False, 2, 3, "ERROR"),
    (1.1, "test", 3, "ERROR"),
    
    # 边界情况
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    (1, 1, 1.0, "EQUILATERAL"),
    (1.0, 1.0, 1.0, "EQUILATERAL"),
    (1.0, 2.0, 2.0, "ISOSCELES"),
    (1.0, 2.0, 3.0, "INVALID"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected