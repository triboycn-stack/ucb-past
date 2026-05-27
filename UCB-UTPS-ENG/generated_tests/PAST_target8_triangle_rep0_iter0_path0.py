# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or (not isinstance(c, (int, float))))
# 重复次数: 0, 迭代: 0
# 生成时间: 2026-04-26 06:50:25

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
    # 三角形不等式定理不满足
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    # 边界值测试
    (1e-9, 1e-9, 1e-9, "EQUILATERAL"),
    (1e-9, 1e-9, 1e-9 + 1e-10, "ISOSCELES"),
    (1, 1, 1.9999999999, "INVALID"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    # 混合类型测试
    (1, 2.0, 2, "ISOSCELES"),
    (2.0, 2, 2.0, "EQUILATERAL"),
    # 非法输入组合
    ("test", "test", "test", "ERROR"),
    (None, None, None, "ERROR"),
    (-1, -1, -1, "INVALID"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected