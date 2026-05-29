# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b == c
# 重复次数: 2, 迭代: 8
# 生成时间: 2026-04-26 06:54:41

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形测试用例
    (3, 3, 3, "EQUILATERAL"),
    (2, 2, 3, "ISOSCELES"),
    (4, 5, 6, "SCALENE"),
    
    # 无效三角形测试用例
    (1, 2, 3, "INVALID"),
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 1, 2, "INVALID"),
    
    # 输入错误测试用例
    ("test", 2, 3, "ERROR"),
    (1, "test", 3, "ERROR"),
    (1, 2, "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    (True, 2, 3, "ERROR"),
    (False, 2, 3, "ERROR"),
    
    # 边界条件测试用例
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1, 1, 1.0, "EQUILATERAL"),
    (1, 2, 2, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    (1, 1, 1, "EQUILATERAL"),
    (1, 2, 2.0, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected