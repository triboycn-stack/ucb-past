# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or (not isinstance(c, (int, float))))
# 重复次数: 4, 迭代: 0
# 生成时间: 2026-04-26 06:56:29

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 输入验证：非数字类型
    ("test", 3, 4, "ERROR"),
    (3, "test", 4, "ERROR"),
    (3, 4, "test", "ERROR"),
    # 输入验证：负数
    (-1, 2, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 3, -1, "INVALID"),
    # 输入验证：零
    (0, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    # 三角形不等式定理：无效三角形
    (1, 2, 3, "INVALID"),
    (2, 3, 5, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (1.5, 1.5, 1.5, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    (1.5, 1.5, 2, "ISOSCELES"),
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
    # 边界条件：最小有效值
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),  # 刚好不满足三角形不等式
    (1, 2, 2, "ISOSCELES"),
    # 边界条件：大数值
    (1000000, 1000000, 1000000, "EQUILATERAL"),
    (1000000, 1000000, 1000001, "ISOSCELES"),
    (1000000, 1000001, 1000002, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected