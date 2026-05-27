# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 4, 迭代: 7
# 生成时间: 2026-04-18 16:08:28

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
    (0, 2, 0, 6.00),
    (0, 0, 4, 5.00),
    (1, 1, 1, 10.00),
    (2, 3, 4, 27.00),

    # 销售额 ≤ 1800 的情况
    (10, 10, 10, 100.00),
    (15, 15, 15, 197.50),
    (20, 20, 20, 340.00),

    # 销售额 > 1800 的情况
    (30, 30, 30, 520.00),
    (40, 40, 40, 820.00),
    (50, 50, 50, 1120.00),

    # 边界值测试
    (0, 0, 0, 0.00),
    (22, 0, 0, 99.00),
    (23, 0, 0, 100.00),
    (40, 0, 0, 160.00),
    (41, 0, 0, 162.00),
    (0, 0, 72, 180.00),
    (0, 0, 73, 182.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected