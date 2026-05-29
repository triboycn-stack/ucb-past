# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a + b <= c or a + c <= b or b + c <= a)
# 重复次数: 3, 迭代: 2
# 生成时间: 2026-04-18 17:25:29

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 4, 5, "SCALENE"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 6, "ISOSCELES"),
    (2, 3, 4, "SCALENE"),
    # 无效三角形（边长为0或负数）
    (0, 4, 5, "INVALID"),
    (-1, 4, 5, "INVALID"),
    (3, 0, 5, "INVALID"),
    # 输入错误（非数字）
    ("test", 4, 5, "ERROR"),
    (3, "test", 5, "ERROR"),
    (3, 4, "test", "ERROR"),
    # 非法输入（字符串）
    ("a", "b", "c", "ERROR"),
    # 边界条件（最小值）
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    # 临界值（刚好满足三角形不等式）
    (1, 1, 1.999, "ISOSCELES"),
    (1, 2, 2.999, "ISOSCELES"),
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 10, "INVALID"),
    # 浮点数测试
    (2.5, 2.5, 2.5, "EQUILATERAL"),
    (2.5, 2.5, 3.0, "ISOSCELES"),
    (2.5, 3.0, 4.0, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected