# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1000
# 重复次数: 0, 迭代: 0
# 生成时间: 2026-04-18 15:50:26

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("invalid", 10, 5, -1.0),
    (10, "invalid", 5, -1.0),
    (10, 10, "invalid", -1.0),
    (10, -5, 5, -1.0),
    (-10, 10, 5, -1.0),
    (10, 10, -5, -1.0),

    # 销售额 <= 1000 的情况
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 3, 27.00),

    # 销售额 <= 1800 的情况
    (10, 10, 10, 145.00),
    (5, 5, 10, 112.50),
    (0, 20, 0, 100.00),
    (0, 0, 60, 100.00),
    (10, 0, 20, 145.00),

    # 销售额 > 1800 的情况
    (20, 20, 20, 220.00),
    (15, 15, 30, 220.00),
    (10, 10, 50, 220.00),
    (0, 0, 100, 220.00),
    (5, 5, 60, 220.00),

    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 1, 25.00),
    (0, 0, 40, 100.00),
    (0, 0, 72, 220.00),
    (0, 0, 73, 220.00 + 25 * 0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected