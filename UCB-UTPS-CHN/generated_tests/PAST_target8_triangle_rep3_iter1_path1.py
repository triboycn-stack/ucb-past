# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or (not isinstance(c, (int, float)))
# 重复次数: 3, 迭代: 1
# 生成时间: 2026-04-26 06:55:10

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
    # 非正数输入
    (-1, 2, 3, "INVALID"),
    (0, 2, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, 2, -3, "INVALID"),
    (1, 2, 0, "INVALID"),
    # 无法构成三角形
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 11, "INVALID"),
    # 等边三角形
    (3, 3, 3, "EQUILATERAL"),
    (1.5, 1.5, 1.5, "EQUILATERAL"),
    # 等腰三角形
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 3, "ISOSCELES"),
    (4, 3, 3, "ISOSCELES"),
    (2.5, 2.5, 3, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2, 3, 4, "SCALENE"),
    (5.5, 6.5, 7.5, "SCALENE"),
    # 边界值测试
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e-9, 1e-9, 1e-9 + 1e-10, "ISOSCELES"),
    (1e-9, 1e-9 + 1e-10, 1e-9 + 2e-10, "SCALENE"),
    # 非数值类型
    (True, 2, 3, "ERROR"),
    (False, 2, 3, "ERROR"),
    (complex(1, 2), 2, 3, "ERROR"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected