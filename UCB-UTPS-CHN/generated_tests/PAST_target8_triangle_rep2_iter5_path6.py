# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a <= 0 or b <= 0 or c <= 0)
# 重复次数: 2, 迭代: 5
# 生成时间: 2026-04-18 17:23:50

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效输入，等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 有效输入，等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 有效输入，不等边三角形
    (3, 4, 5, "SCALENE"),
    # 无效输入（负数）
    (-1, 2, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 2, -3, "INVALID"),
    # 无效输入（零）
    (0, 2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, 2, 0, "INVALID"),
    # 无效输入（非数字）
    ("a", 2, 3, "ERROR"),
    (1, "b", 3, "ERROR"),
    (1, 2, "c", "ERROR"),
    # 无效输入（字符串）
    ("test", "test", "test", "ERROR"),
    # 无效三角形（两边之和不大于第三边）
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 边界情况（最小值）
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    # 边界情况（最大值）
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    # 有效输入，等腰但非等边
    (5, 5, 6, "ISOSCELES"),
    # 有效输入，不等边
    (4, 5, 6, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected