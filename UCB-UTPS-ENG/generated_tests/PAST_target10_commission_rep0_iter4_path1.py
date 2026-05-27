# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 0, 迭代: 4
# 生成时间: 2026-04-18 15:52:19

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
    (10.5, 10, 10, -1.0),
    (10, 10.5, 10, -1.0),
    (10, 10, 10.5, -1.0),

    # 销售额 ≤ 1000 的情况
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 1, 16.50),

    # 销售额 ≤ 1800 的情况
    (10, 10, 10, 175.00),
    (5, 5, 5, 67.50),
    (15, 15, 15, 255.00),

    # 销售额 > 1800 的情况
    (20, 20, 20, 340.00),
    (30, 30, 30, 520.00),
    (100, 100, 100, 2200.00),

    # 边界值测试
    (0, 0, 0, 0.00),
    (22, 0, 0, 99.00),
    (23, 0, 0, 100.00 + (23*45 - 1000)*0.15),
    (40, 0, 0, 220 + (40*45 - 1800)*0.20),
    (40, 0, 0, 220 + (1800 - 1800)*0.20),
    (41, 0, 0, 220 + (41*45 - 1800)*0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected