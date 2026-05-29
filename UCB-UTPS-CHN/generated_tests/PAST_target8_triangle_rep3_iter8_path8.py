# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b == c
# 重复次数: 3, 迭代: 8
# 生成时间: 2026-04-26 06:56:09

import pytest
from target8_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    # 有效三角形 - 等边
    (3.0, 3.0, 3.0, "EQUILATERAL"),
    # 有效三角形 - 等腰
    (3.0, 3.0, 4.0, "ISOSCELES"),
    (3.0, 4.0, 3.0, "ISOSCELES"),
    (4.0, 3.0, 3.0, "ISOSCELES"),
    # 有效三角形 - 不等边
    (3.0, 4.0, 5.0, "SCALENE"),
    # 无效三角形 - 边长为0
    (0.0, 3.0, 4.0, "INVALID"),
    (3.0, 0.0, 4.0, "INVALID"),
    (3.0, 4.0, 0.0, "INVALID"),
    # 无效三角形 - 负数
    (-1.0, 3.0, 4.0, "INVALID"),
    (3.0, -1.0, 4.0, "INVALID"),
    (3.0, 4.0, -1.0, "INVALID"),
    # 无效三角形 - 不满足三角形不等式
    (1.0, 2.0, 3.0, "INVALID"),
    (2.0, 3.0, 6.0, "INVALID"),
    (3.0, 4.0, 8.0, "INVALID"),
    # 输入错误 - 非数字类型
    ("test", 3.0, 4.0, "ERROR"),
    (3.0, "test", 4.0, "ERROR"),
    (3.0, 4.0, "test", "ERROR"),
    # 输入错误 - 非数值类型
    (None, 3.0, 4.0, "ERROR"),
    (3.0, None, 4.0, "ERROR"),
    (3.0, 4.0, None, "ERROR"),
    # 边界情况 - 极小值
    (0.0001, 0.0001, 0.0001, "EQUILATERAL"),
    (0.0001, 0.0001, 0.0002, "ISOSCELES"),
    (0.0001, 0.0002, 0.0003, "INVALID"),
    # 边界情况 - 极大值
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 + 1, "ISOSCELES"),
    (1e10, 1e10 + 1, 2e10, "INVALID"),
    # 特殊情况 - 三边相等但为浮点数
    (2.5, 2.5, 2.5, "EQUILATERAL"),
    # 特殊情况 - 三边不等但接近相等
    (2.0, 2.0, 2.0000001, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected