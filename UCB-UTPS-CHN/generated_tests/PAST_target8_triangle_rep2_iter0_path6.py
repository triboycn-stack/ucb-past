# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a <= 0 or b <= 0 or c <= 0)
# 重复次数: 2, 迭代: 0
# 生成时间: 2026-04-18 17:23:09

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
    (1, 2, 2, "ISOSCELES"),
    (1, 1, 2, "INVALID"),  # 不满足三角形不等式
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (0.1, 0.2, 0.2, "ISOSCELES"),
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
    # 非数值类型
    ("a", "b", "c", "ERROR"),
    (True, 2, 3, "ERROR"),
    (2, True, 3, "ERROR"),
    (2, 3, True, "ERROR"),
    # 等腰三角形边界
    (2, 2, 2.0, "EQUILATERAL"),
    (2, 2, 3.0, "ISOSCELES"),
    # 等边三角形边界
    (1.0, 1.0, 1.0, "EQUILATERAL"),
    # 不等边三角形边界
    (1.1, 2.2, 3.3, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected