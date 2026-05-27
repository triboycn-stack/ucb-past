# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a + b <= c or a + c <= b or b + c <= a
# 重复次数: 4, 迭代: 2
# 生成时间: 2026-04-26 06:56:45

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 4, 5, "SCALENE"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 6, "ISOSCELES"),
    (2, 2, 3, "ISOSCELES"),
    (7, 8, 9, "SCALENE"),
    # 无效三角形（边长不符合三角形不等式）
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 10, "INVALID"),
    # 输入错误（非数字类型）
    ("test", 2, 3, "ERROR"),
    (1, "test", 3, "ERROR"),
    (1, 2, "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    # 边界值测试
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    # 零或负数
    (-1, 2, 3, "INVALID"),
    (0, 2, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 2, 0, "INVALID"),
    # 等腰三角形边界情况
    (2, 2, 2.0, "EQUILATERAL"),
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 不等边三角形边界情况
    (1.1, 2.2, 3.3, "SCALENE"),
    (1.0, 2.0, 3.0, "SCALENE"),
    # 条件分支覆盖（a + b <= c）
    (1, 1, 3, "INVALID"),
    # 条件分支覆盖（a + c <= b）
    (1, 3, 1, "INVALID"),
    # 条件分支覆盖（b + c <= a）
    (3, 1, 1, "INVALID"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected