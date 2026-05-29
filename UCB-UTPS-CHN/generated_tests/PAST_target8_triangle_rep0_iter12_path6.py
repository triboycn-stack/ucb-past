# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a <= 0 or b <= 0 or c <= 0)
# 重复次数: 0, 迭代: 12
# 生成时间: 2026-04-18 17:20:42

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效输入，等边三角形
    (3, 3, 3, "EQUILATERAL"),
    # 有效输入，等腰三角形
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 3, "ISOSCELES"),
    (4, 3, 3, "ISOSCELES"),
    # 有效输入，不等边三角形
    (3, 4, 5, "SCALENE"),
    # 无效输入，负数
    (-1, 2, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 3, -1, "INVALID"),
    # 无效输入，零
    (0, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    # 无效输入，非数字
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    # 无效输入，不符合三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 边界条件：最小值
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    # 边界条件：最大值（假设为浮点数）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    (1e100, 1e100, 1e100 - 1, "ISOSCELES"),
    (1e100, 1e100 + 1, 1e100, "INVALID"),
    # 非数字类型
    (None, 2, 3, "ERROR"),
    (2, None, 3, "ERROR"),
    (2, 3, None, "ERROR"),
    # 浮点数
    (2.5, 2.5, 2.5, "EQUILATERAL"),
    (2.5, 2.5, 3.0, "ISOSCELES"),
    (2.5, 3.0, 4.0, "SCALENE"),
    # 大数值
    (1000000, 1000000, 1000000, "EQUILATERAL"),
    (1000000, 1000000, 1000001, "ISOSCELES"),
    (1000000, 1000001, 1000002, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected