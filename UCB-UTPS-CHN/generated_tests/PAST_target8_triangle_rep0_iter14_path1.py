# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or (not isinstance(c, (int, float)))
# 重复次数: 0, 迭代: 14
# 生成时间: 2026-04-18 17:20:58

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证：非数字类型
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    # 输入验证：负数
    (-1, 2, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 3, -1, "INVALID"),
    # 输入验证：零
    (0, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    # 三角形不等式定理：无效三角形
    (1, 2, 3, "INVALID"),
    (2, 3, 5, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 不等边三角形
    (2, 3, 4, "SCALENE"),
    # 边界条件：最小值
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    # 边界条件：最大值（假设为浮点数）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    (1e100, 1e100, 1e100 - 1, "ISOSCELES"),
    (1e100, 1e100 + 1, 1e100 + 2, "SCALENE"),
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