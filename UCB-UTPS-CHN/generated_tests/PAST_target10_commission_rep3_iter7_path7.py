# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1800
# 重复次数: 3, 迭代: 7
# 生成时间: 2026-04-26 07:20:57

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("hello", 10, 20, -1.0),
    (10, "world", 20, -1.0),
    (10, 20, "foo", -1.0),
    (10.5, 20, 30, -1.0),
    (10, 20.5, 30, -1.0),
    (10, 20, 30.5, -1.0),
    (-1, 10, 20, -1.0),
    (10, -5, 20, -1.0),
    (10, 20, -3, -1.0),

    # 销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 2, 0, 6.00),
    (0, 0, 4, 5.00),
    (2, 1, 1, 14.50),

    # 销售额 <= 1800
    (10, 10, 10, 175.00),
    (5, 15, 10, 195.00),
    (0, 30, 0, 180.00),
    (10, 0, 20, 170.00),

    # 销售额 > 1800
    (20, 20, 20, 260.00),
    (15, 25, 20, 280.00),
    (0, 40, 0, 220.00),
    (10, 0, 40, 220.00),

    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 1, 2.50),
    (0, 0, 40, 1000.00),
    (0, 0, 41, 1025.00),
    (0, 0, 60, 1500.00),
    (0, 0, 72, 1800.00),
    (0, 0, 73, 1820.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected