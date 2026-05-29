# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a <= 0 or b <= 0 or c <= 0
# 重复次数: 2, 迭代: 9
# 生成时间: 2026-04-18 17:24:21

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证错误
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    (2, None, 3, "ERROR"),
    (2, 3, None, "ERROR"),
    # 零或负数边长
    (0, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 3, -1, "INVALID"),
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 5, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (3.5, 3.5, 3.5, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (5.5, 5.5, 6, "ISOSCELES"),
    # 不等边三角形
    (2, 3, 4, "SCALENE"),
    (3, 4, 5, "SCALENE"),
    (5.1, 6.2, 7.3, "SCALENE"),
    # 边界情况
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e-9, 1e-9, 1e-9 + 1e-10, "ISOSCELES"),
    (1e9, 1e9, 1e9, "EQUILATERAL"),
    (1e9, 1e9, 1e9 + 1, "ISOSCELES"),
    # 特殊值
    (0.0, 0.0, 0.0, "INVALID"),
    (1.0, 1.0, 1.0, "EQUILATERAL"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected