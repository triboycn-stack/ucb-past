# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b == c)
# 重复次数: 1, 迭代: 1
# 生成时间: 2026-04-18 17:21:14

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入：非数字类型
    ("test", "test", "test", "ERROR"),
    (None, 1, 2, "ERROR"),
    (1, None, 2, "ERROR"),
    (1, 2, None, "ERROR"),
    
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
    (3, 4, 8, "INVALID"),
    (5, 5, 11, "INVALID"),
    
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
    (2, 3, 4, "SCALENE"),
    (5, 7, 9, "SCALENE"),
    (1.5, 2.5, 3.5, "SCALENE"),
    
    # 边界条件：最小值
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    
    # 边界条件：最大值（假设为浮点数最大值）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    (1e100, 1e100, 1e100 + 1, "INVALID"),
    (1e100, 1e100 + 1, 1e100 + 1, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected