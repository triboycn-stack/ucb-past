# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b == c)
# 重复次数: 2, 迭代: 8
# 生成时间: 2026-04-18 17:24:11

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入：非数字类型
    ("test", "test", "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (3.14, "string", 5, "ERROR"),
    
    # 无效输入：边长为0或负数
    (-1, 2, 3, "INVALID"),
    (0, 4, 5, "INVALID"),
    (2, -3, 4, "INVALID"),
    
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 11, "INVALID"),
    
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
    
    # 边界条件：最小有效值
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (0.1, 0.1, 0.2, "ISOSCELES"),
    (0.1, 0.2, 0.3, "INVALID"),
    
    # 边界条件：最大有效值（假设为1e6）
    (1e6, 1e6, 1e6, "EQUILATERAL"),
    (1e6, 1e6, 1e6 - 1, "ISOSCELES"),
    (1e6, 1e6 - 1, 1e6 - 2, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected