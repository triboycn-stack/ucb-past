# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b == c)
# 重复次数: 0, 迭代: 2
# 生成时间: 2026-04-18 17:19:20

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形 - 等边
    (2, 2, 2, "EQUILATERAL"),
    # 有效三角形 - 等腰
    (2, 2, 3, "ISOSCELES"),
    (2, 3, 2, "ISOSCELES"),
    (3, 2, 2, "ISOSCELES"),
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
    (2, "b", 3, "ERROR"),
    (2, 3, "c", "ERROR"),
    # 输入错误 - 非数值类型
    (None, 2, 3, "ERROR"),
    (True, 2, 3, "ERROR"),
    (False, 2, 3, "ERROR"),
    # 边界情况 - 极小值
    (0.0001, 0.0001, 0.0001, "EQUILATERAL"),
    (0.0001, 0.0001, 0.0002, "ISOSCELES"),
    (0.0001, 0.0002, 0.0003, "INVALID"),
    # 边界情况 - 极大值
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 + 1, "ISOSCELES"),
    (1e10, 1e10 + 1, 1e10 + 2, "INVALID"),
    # 条件分支覆盖 - not (a == b == c)
    (2, 3, 4, "SCALENE"),
    (2, 3, 3, "ISOSCELES"),
    (2, 2, 3, "ISOSCELES"),
    (3, 3, 3, "EQUILATERAL"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected