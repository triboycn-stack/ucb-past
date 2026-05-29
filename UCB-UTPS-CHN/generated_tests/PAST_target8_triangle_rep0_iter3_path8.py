# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: a == b == c
# 重复次数: 0, 迭代: 3
# 生成时间: 2026-04-18 17:19:28

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
    # 无效三角形 - 边长为0或负数
    (0, 1, 2, "INVALID"),
    (-1, 2, 3, "INVALID"),
    # 无效三角形 - 不满足三角形不等式
    (1, 2, 3, "INVALID"),
    (2, 3, 6, "INVALID"),
    # 输入错误 - 非数字类型
    ("test", 2, 3, "ERROR"),
    (1, "test", 3, "ERROR"),
    (1, 2, "test", "ERROR"),
    # 边界情况 - 极小值
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (0.1, 0.1, 0.2, "ISOSCELES"),
    (0.1, 0.2, 0.3, "INVALID"),
    # 边界情况 - 极大值
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 + 1, "ISOSCELES"),
    (1e10, 1e10 + 1, 1e10 + 2, "SCALENE"),
    # 特殊情况 - 三边相等但为浮点数
    (2.0, 2.0, 2.0, "EQUILATERAL"),
    # 浮点数精度问题
    (1.0, 1.0, 1.0000000001, "ISOSCELES"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected