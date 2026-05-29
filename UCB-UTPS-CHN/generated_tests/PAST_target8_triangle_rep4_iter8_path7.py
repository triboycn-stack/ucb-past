# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b or b == c or a == c)
# 重复次数: 4, 迭代: 8
# 生成时间: 2026-04-18 17:28:54

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入
    ("test", "test", "test", "ERROR"),
    (None, 1, 2, "ERROR"),
    (1.0, "test", 3, "ERROR"),
    # 零或负数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    (1, 0, 2, "INVALID"),
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 11, "INVALID"),
    # 等边三角形
    (2, 2, 2, "EQUILATERAL"),
    (1.5, 1.5, 1.5, "EQUILATERAL"),
    # 等腰三角形
    (2, 2, 3, "ISOSCELES"),
    (3, 4, 4, "ISOSCELES"),
    (5, 5, 5.0, "EQUILATERAL"),  # 等边但类型不同
    # 不等边三角形
    (3, 4, 5, "SCALENE"),
    (2.1, 3.2, 4.3, "SCALENE"),
    # 边界情况：最小有效值
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (0.1, 0.1, 0.2, "ISOSCELES"),
    (0.1, 0.2, 0.3, "INVALID"),
    # 条件分支覆盖：not (a == b or b == c or a == c)
    (3, 4, 5, "SCALENE"),
    (2.5, 3.5, 4.5, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected