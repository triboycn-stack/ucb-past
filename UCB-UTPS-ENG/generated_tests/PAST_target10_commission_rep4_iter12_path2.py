# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: locks < 0 or stocks < 0 or barrels < 0
# 重复次数: 4, 迭代: 12
# 生成时间: 2026-04-18 16:09:53

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (10, 10, -5, -1.0),
    (-5, 10, 10, -1.0),
    (10, -5, 10, -1.0),
    (10, 10, -5, -1.0),
    (10, 10, 10, -1.0),  # 非整数输入（字符串）导致返回-1.0

    # 销售额 ≤ 1000 的情况
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 1, 13.50),

    # 销售额 ≤ 1800 的情况
    (10, 10, 10, 160.00),
    (15, 10, 10, 227.50),
    (20, 10, 10, 300.00),
    (0, 20, 10, 220.00),

    # 销售额 > 1800 的情况
    (30, 10, 10, 380.00),
    (40, 10, 10, 500.00),
    (50, 10, 10, 620.00),
    (0, 30, 10, 340.00),

    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 1, 25.00),
    (0, 0, 40, 100.00),
    (0, 0, 41, 102.50),
    (0, 0, 72, 220.00),
    (0, 0, 73, 225.00),
    (0, 0, 100, 320.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert round(result, 2) == round(expected, 2)