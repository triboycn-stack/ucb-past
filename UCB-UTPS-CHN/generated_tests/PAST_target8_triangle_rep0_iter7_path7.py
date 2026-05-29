# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b or b == c or a == c)
# 重复次数: 0, 迭代: 7
# 生成时间: 2026-04-26 06:51:26

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 无效输入：非数字类型
    ("test", 2, 3, "ERROR"),
    (2, "test", 3, "ERROR"),
    (2, 3, "test", "ERROR"),
    # 无效输入：负数
    (-1, 2, 3, "INVALID"),
    (2, -1, 3, "INVALID"),
    (2, 3, -1, "INVALID"),
    # 无效输入：零
    (0, 2, 3, "INVALID"),
    (2, 0, 3, "INVALID"),
    (2, 3, 0, "INVALID"),
    # 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 5, "INVALID"),
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
    # 边界情况：最小值
    (1, 1, 1, "EQUILATERAL"),
    (1, 1, 2, "INVALID"),
    (1, 2, 2, "ISOSCELES"),
    # 边界情况：最大值
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 + 1, "ISOSCELES"),
    (1e10, 1e10 + 1, 1e10 + 2, "SCALENE"),
    # 异常情况：非数值输入
    (None, 2, 3, "ERROR"),
    (True, 2, 3, "ERROR"),
    (False, 2, 3, "ERROR"),
    # 满足条件分支：not (a == b or b == c or a == c)
    (3, 4, 5, "SCALENE"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected