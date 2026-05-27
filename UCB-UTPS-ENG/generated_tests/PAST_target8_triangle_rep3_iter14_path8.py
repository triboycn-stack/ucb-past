# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b == c
# 重复次数: 3, 迭代: 14
# 生成时间: 2026-04-18 17:27:41

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形 - 等边
    (3, 3, 3, "EQUILATERAL"),
    # 有效三角形 - 等腰
    (3, 3, 4, "ISOSCELES"),
    (3, 4, 3, "ISOSCELES"),
    (4, 3, 3, "ISOSCELES"),
    # 有效三角形 - 不等边
    (3, 4, 5, "SCALENE"),
    # 无效三角形 - 边长为0
    (0, 1, 2, "INVALID"),
    (1, 0, 2, "INVALID"),
    (1, 2, 0, "INVALID"),
    # 无效三角形 - 负数
    (-1, 2, 3, "INVALID"),
    (1, -2, 3, "INVALID"),
    (1, 2, -3, "INVALID"),
    # 无效三角形 - 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    (3, 4, 8, "INVALID"),
    # 输入错误 - 非数字类型
    ("a", 2, 3, "ERROR"),
    (1, "b", 3, "ERROR"),
    (1, 2, "c", "ERROR"),
    # 输入错误 - 非数值类型
    (None, 2, 3, "ERROR"),
    (True, 2, 3, "ERROR"),
    (False, 2, 3, "ERROR"),
    # 边界情况 - 极小值
    (0.0000001, 0.0000001, 0.0000001, "EQUILATERAL"),
    # 边界情况 - 极大值
    (1e100, 1e100, 1e100, "EQUILATERAL"),
    # 特殊情况 - 等边但有浮点精度问题
    (1.0, 1.0, 1.0, "EQUILATERAL"),
    (1.0, 1.0, 1.0000000001, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected