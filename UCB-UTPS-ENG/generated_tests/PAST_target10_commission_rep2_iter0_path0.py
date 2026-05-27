# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 2, 迭代: 0
# 生成时间: 2026-04-26 07:16:12

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (2, 0, 0, 9.00),
    (0, 3, 0, 9.00),
    (0, 0, 4, 10.00),
    (1, 1, 1, 10.00),
    # 有效输入，销售额在 1000-1800 之间
    (10, 10, 10, 100.00),
    (15, 10, 10, 122.50),
    (20, 10, 10, 145.00),
    (10, 20, 10, 145.00),
    # 有效输入，销售额 > 1800
    (30, 0, 0, 220.00),
    (20, 10, 10, 220.00),
    (25, 10, 10, 265.00),
    (10, 25, 10, 265.00),
    (10, 10, 25, 265.00),
    # 边界值测试
    (0, 0, 0, 0.00),
    (22, 0, 0, 99.00),  # 22 * 45 = 990 → 990 * 0.10 = 99.00
    (23, 0, 0, 100.00 + (1035 - 1000) * 0.15)  # 23 * 45 = 1035 → 100 + 35*0.15 = 105.25
    # 无效输入
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    (0.0, 0, 0, -1.0),
    (0, 0.0, 0, -1.0),
    (0, 0, 0.0, -1.0),
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    (None, 0, 0, -1.0),
    (0, None, 0, -1.0),
    (0, 0, None, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected