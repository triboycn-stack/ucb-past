# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 2, 迭代: 11
# 生成时间: 2026-04-18 16:01:04

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
    (10.5, 20, 30, -1.0),
    (10, "20", 30, -1.0),
    (10, 20, 30.5, -1.0),
    (10, -5, 30, -1.0),
    (-10, 20, 30, -1.0),
    (10, 20, -5, -1.0),

    # 销售额 ≤ 1000 的情况
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 3, 18.00),

    # 销售额 ≤ 1800 的情况
    (10, 10, 10, 100.00),
    (15, 10, 10, 122.50),
    (20, 10, 10, 145.00),
    (0, 30, 0, 180.00),
    (0, 0, 72, 180.00),

    # 销售额 > 1800 的情况
    (20, 20, 20, 220.00),
    (30, 20, 20, 265.00),
    (0, 60, 0, 220.00),
    (0, 0, 120, 220.00),
    (10, 10, 50, 265.00),

    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 1, 25.00),
    (0, 0, 40, 100.00),
    (0, 0, 72, 180.00),
    (0, 0, 73, 220.00),
    (0, 0, 100, 220.00),
    (0, 0, 101, 220.00 + 25 * 0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected