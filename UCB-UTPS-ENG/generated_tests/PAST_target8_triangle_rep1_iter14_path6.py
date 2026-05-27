# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a <= 0 or b <= 0 or c <= 0)
# 重复次数: 1, 迭代: 14
# 生成时间: 2026-04-18 17:23:00

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效输入，等边三角形
    (2, 2, 2, "EQUILATERAL"),
    # 有效输入，等腰三角形
    (3, 3, 4, "ISOSCELES"),
    (5, 4, 5, "ISOSCELES"),
    (4, 5, 5, "ISOSCELES"),
    # 有效输入，不等边三角形
    (3, 4, 5, "SCALENE"),
    (5, 6, 7, "SCALENE"),
    # 无效输入（负数）
    (-1, 2, 3, "INVALID"),
    (2, -3, 4, "INVALID"),
    (5, 6, -7, "INVALID"),
    # 无效输入（零）
    (0, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    # 无效输入（非数字）
    ("a", 2, 3, "ERROR"),
    (1, "b", 3, "ERROR"),
    (1, 2, "c", "ERROR"),
    # 无效输入（非数值类型）
    (None, 2, 3, "ERROR"),
    (True, 2, 3, "ERROR"),
    (False, 2, 3, "ERROR"),
    # 无效输入（字符串）
    ("1", "2", "3", "ERROR"),
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (5, 5, 11, "INVALID"),
    # 边界情况：最小有效值
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (0.1, 0.1, 0.2, "ISOSCELES"),
    (0.1, 0.2, 0.3, "INVALID"),
    # 边界情况：最大有效值
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 - 1, "ISOSCELES"),
    (1e10, 1e10 - 1, 1e10 - 2, "SCALENE"),
    # 非法输入（混合类型）
    (1, "2", 3, "ERROR"),
    (1, 2, True, "ERROR"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected