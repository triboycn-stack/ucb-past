# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (locks < 0 or stocks < 0 or barrels < 0)
# 重复次数: 4, 迭代: 3
# 生成时间: 2026-04-26 07:22:00

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    (23, 0, 0, 103.50),
    # 有效输入，销售额 <= 1800
    (40, 0, 0, 100.00),
    (41, 0, 0, 101.50),
    (60, 0, 0, 175.00),
    (61, 0, 0, 177.25),
    # 有效输入，销售额 > 1800
    (80, 0, 0, 220.00),
    (81, 0, 0, 223.00),
    (100, 0, 0, 260.00),
    (101, 0, 0, 264.20),
    # 输入验证：非整数
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "foo", -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况：销售额刚好为1000
    (22, 0, 0, 99.00),
    (23, 0, 0, 103.50),
    # 边界情况：销售额刚好为1800
    (40, 0, 0, 100.00),
    (41, 0, 0, 101.50),
    # 非法输入（字符串）
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    # 非法输入（浮点数）
    (1.5, 0, 0, -1.0),
    (0, 2.5, 0, -1.0),
    (0, 0, 3.5, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected