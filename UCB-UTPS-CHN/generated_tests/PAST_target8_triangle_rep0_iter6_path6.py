# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a <= 0 or b <= 0 or c <= 0)
# 重复次数: 0, 迭代: 6
# 生成时间: 2026-04-26 06:51:18

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形
    (3, 4, 5, "SCALENE"),
    (5, 5, 5, "EQUILATERAL"),
    (5, 5, 6, "ISOSCELES"),
    (2, 2, 3, "ISOSCELES"),
    (7, 8, 9, "SCALENE"),
    # 边界条件
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (0.1, 0.2, 0.3, "INVALID"),
    # 非法输入
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    (None, 2, 3, "ERROR"),
    (2, None, 3, "ERROR"),
    (2, 3, None, "ERROR"),
    # 负数
    (-1, 2, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 3, -1, "INVALID"),
    # 零值
    (0, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 等腰但非等边
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
    # 等边
    (5, 5, 5, "EQUILATERAL"),
    # 不等边
    (4, 5, 6, "SCALENE"),
    # 浮点数
    (1.5, 1.5, 1.5, "EQUILATERAL"),
    (1.5, 2.5, 3.0, "SCALENE"),
    (2.0, 2.0, 3.0, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected