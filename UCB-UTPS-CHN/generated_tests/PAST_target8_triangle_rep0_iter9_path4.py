# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a <= 0 or b <= 0 or c <= 0
# 重复次数: 0, 迭代: 9
# 生成时间: 2026-04-18 17:20:17

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入：非数字类型
    ("test", 3, 4, "ERROR"),
    (3, "test", 4, "ERROR"),
    (3, 4, "test", "ERROR"),
    # 无效输入：边长为0或负数
    (0, 4, 5, "INVALID"),
    (-1, 4, 5, "INVALID"),
    (3, 0, 5, "INVALID"),
    (3, -2, 5, "INVALID"),
    (3, 4, 0, "INVALID"),
    (3, 4, -3, "INVALID"),
    # 三角形不等式定理不满足
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 11, "INVALID"),
    # 等边三角形
    (3, 3, 3, "EQUILATERAL"),
    # 等腰三角形
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 3, "ISOSCELES"),
    (4, 3, 3, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    # 边界条件：最小值
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (0.1, 0.1, 0.2, "ISOSCELES"),
    (0.1, 0.2, 0.3, "INVALID"),
    # 边界条件：最大值（浮点数）
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 - 1, "ISOSCELES"),
    (1e10, 1e10 - 1, 1e10 - 2, "SCALENE"),
    # 非法输入：字符串
    ("a", "b", "c", "ERROR"),
    # 非法输入：None
    (None, 3, 4, "ERROR"),
    (3, None, 4, "ERROR"),
    (3, 4, None, "ERROR"),
    # 非法输入：布尔值
    (True, 3, 4, "ERROR"),
    (3, True, 4, "ERROR"),
    (3, 4, True, "ERROR"),
    # 非法输入：列表
    ([1, 2], 3, 4, "ERROR"),
    (1, [2, 3], 4, "ERROR"),
    (1, 2, [3, 4], "ERROR"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected