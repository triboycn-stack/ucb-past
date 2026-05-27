# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or (not isinstance(c, (int, float)))
# 重复次数: 0, 迭代: 4
# 生成时间: 2026-04-18 17:19:36

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证错误
    ("test", 3, 4, "ERROR"),
    (3, "test", 4, "ERROR"),
    (3, 4, "test", "ERROR"),
    (None, 3, 4, "ERROR"),
    (3, None, 4, "ERROR"),
    (3, 4, None, "ERROR"),
    # 零或负数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 2, "INVALID"),
    (1, -1, 2, "INVALID"),
    (1, 2, 0, "INVALID"),
    (1, 2, -1, "INVALID"),
    # 三角形不等式定理失败
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
    (3.5, 3.5, 4, "ISOSCELES"),
    (3.5, 4, 3.5, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
    # 边界情况
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "ISOSCELES"),
    (1, 2, 2, "ISOSCELES"),
    (2, 2, 3, "ISOSCELES"),
    (1, 2, 3, "INVALID"),
    (1, 1, 1.0, "EQUILATERAL"),
    (1.0, 1.0, 1.0, "EQUILATERAL"),
    (1.0, 2.0, 2.0, "ISOSCELES"),
    (1.0, 2.0, 3.0, "INVALID"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected