# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a <= 0 or b <= 0 or c <= 0
# 重复次数: 4, 迭代: 5
# 生成时间: 2026-04-18 17:28:30

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    (2, None, 3, "ERROR"),
    (2, 3, None, "ERROR"),
    # 零或负数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 3, "INVALID"),
    (1, 2, -1, "INVALID"),
    # 三角形不等式定理
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 10, "INVALID"),
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
    (1, 1, 1.9999999999, "ISOSCELES"),
    (1, 2, 2.9999999999, "ISOSCELES"),
    (1, 2, 3.0, "INVALID"),
    # 浮点数精度问题
    (1.0, 1.0, 1.0, "EQUILATERAL"),
    (1.0, 1.0, 1.0000000001, "ISOSCELES"),
    (1.0, 2.0, 2.0, "ISOSCELES"),
    (1.0, 2.0, 3.0, "INVALID"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected