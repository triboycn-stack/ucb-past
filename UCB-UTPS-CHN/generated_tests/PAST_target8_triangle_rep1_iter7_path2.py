# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a + b <= c or a + c <= b or b + c <= a
# 重复次数: 1, 迭代: 7
# 生成时间: 2026-04-18 17:22:06

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入：非数字类型
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    # 无效输入：负数
    (-1, 2, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 3, -1, "INVALID"),
    # 无效输入：零
    (0, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    # 三角形不等式不满足
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
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    # 边界条件：最大值（假设为1e6）
    (1e6, 1e6, 1e6, "EQUILATERAL"),
    (1e6, 1e6, 1e6 + 1, "INVALID"),
    # 非法输入：字符串
    ("a", "b", "c", "ERROR"),
    # 非法输入：None
    (None, 2, 3, "ERROR"),
    (2, None, 3, "ERROR"),
    (2, 3, None, "ERROR"),
    # 非法输入：布尔值
    (True, 2, 3, "ERROR"),
    (2, True, 3, "ERROR"),
    (2, 3, True, "ERROR"),
    # 非法输入：列表
    ([1], 2, 3, "ERROR"),
    (2, [1], 3, "ERROR"),
    (2, 3, [1], "ERROR"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected