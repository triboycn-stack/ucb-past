# 方法: PAST
# 目标文件: target8_triangle.py
# 条件路径: not (a == b == c)
# 重复次数: 0, 迭代: 9
# 生成时间: 2026-04-26 06:51:45

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
    (0.0, 1.0, 2.0, "INVALID"),
    (1.0, 0.0, 2.0, "INVALID"),
    (1.0, 2.0, 0.0, "INVALID"),
    # 无效三角形 - 负数
    (-1.0, 2.0, 3.0, "INVALID"),
    (1.0, -2.0, 3.0, "INVALID"),
    (1.0, 2.0, -3.0, "INVALID"),
    # 无效三角形 - 不满足三角形不等式
    (1.0, 2.0, 3.0, "INVALID"),
    (2.0, 3.0, 6.0, "INVALID"),
    (5.0, 5.0, 10.0, "INVALID"),
    # 输入错误 - 非数字类型
    ("test", 2.0, 3.0, "ERROR"),
    (2.0, "test", 3.0, "ERROR"),
    (2.0, 3.0, "test", "ERROR"),
    # 输入错误 - 非数值类型
    (None, 2.0, 3.0, "ERROR"),
    (True, 2.0, 3.0, "ERROR"),
    (False, 2.0, 3.0, "ERROR"),
    # 边界情况 - 极小值
    (0.1, 0.1, 0.1, "EQUILATERAL"),
    (0.1, 0.1, 0.2, "ISOSCELES"),
    (0.1, 0.2, 0.3, "INVALID"),
    # 边界情况 - 极大值
    (1e10, 1e10, 1e10, "EQUILATERAL"),
    (1e10, 1e10, 1e10 + 1, "ISOSCELES"),
    (1e10, 1e10 + 1, 1e10 + 2, "SCALENE"),
    # 临界值 - 刚好满足三角形不等式
    (1.0, 1.0, 1.999, "ISOSCELES"),
    (1.0, 1.0, 2.0, "INVALID"),
    # 临界值 - 刚好不满足三角形不等式
    (1.0, 1.0, 2.001, "INVALID"),
])
def test_classify_triangle(a, b, c, expected):
    result = classify_triangle(a, b, c)
    assert result == expected