# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a + b <= c or a + c <= b or b + c <= a)
# 重复次数: 0, 迭代: 3
# 生成时间: 2026-04-26 06:50:54

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 4, 5, "SCALENE"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 6, "ISOSCELES"),
    (2, 2, 3, "ISOSCELES"),
    (7, 8, 9, "SCALENE"),
    # 无效三角形（边长为0）
    (0, 4, 5, "INVALID"),
    (4, 0, 5, "INVALID"),
    (4, 5, 0, "INVALID"),
    # 无效三角形（边长为负数）
    (-1, 4, 5, "INVALID"),
    (4, -1, 5, "INVALID"),
    (4, 5, -1, "INVALID"),
    # 无效三角形（不满足三角形不等式）
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 输入错误（非数字类型）
    ("test", 4, 5, "ERROR"),
    (4, "test", 5, "ERROR"),
    (4, 5, "test", "ERROR"),
    # 边界情况（最小值）
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    # 边界情况（最大值）
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    (1e100, 1e100, 1e100 + 1, "ISOSCELES"),
    # 非整数但合法的浮点数
    (2.5, 2.5, 2.5, "EQUILATERAL"),
    (2.5, 2.5, 3.0, "ISOSCELES"),
    (2.5, 3.0, 4.0, "SCALENE"),
    # 非法输入（字符串）
    ("a", "b", "c", "ERROR"),
    # 非法输入（None）
    (None, 4, 5, "ERROR"),
    (4, None, 5, "ERROR"),
    (4, 5, None, "ERROR"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected