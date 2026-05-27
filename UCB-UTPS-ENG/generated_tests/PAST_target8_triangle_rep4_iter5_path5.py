# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b or b == c or a == c
# 重复次数: 4, 迭代: 5
# 生成时间: 2026-04-26 06:57:09

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入：非数字类型
    ("test", "test", "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (3, None, 4, "ERROR"),
    (3, 4, None, "ERROR"),
    
    # 无效输入：边长小于等于0
    (-1, 2, 3, "INVALID"),
    (0, 2, 3, "INVALID"),
    (1, -1, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, 2, -1, "INVALID"),
    (1, 2, 0, "INVALID"),
    
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 11, "INVALID"),
    (1, 1, 3, "INVALID"),
    
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (3.5, 3.5, 3.5, "EQUILATERAL"),
    
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (5, 5, 5.0, "EQUILATERAL"),  # 浮点数与整数相等
    
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2.1, 3.2, 4.3, "SCALENE"),
    
    # 边界情况：最小有效值
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "ISOSCELES"),
    (1, 2, 2, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    
    # 边界情况：最大值（假设为浮点数）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    (1e100, 1e100, 1e100 - 1, "ISOSCELES"),
    (1e100, 1e100 + 1, 1e100 + 2, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected