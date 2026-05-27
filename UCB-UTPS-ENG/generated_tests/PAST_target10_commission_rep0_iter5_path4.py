# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales <= 1000)
# 重复次数: 0, 迭代: 5
# 生成时间: 2026-04-18 15:52:28

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("invalid", 1, 1, -1.0),
    (1, "invalid", 1, -1.0),
    (1, 1, "invalid", -1.0),
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    ("1", 1, 1, -1.0),
    (1, "1", 1, -1.0),
    (1, 1, "1", -1.0),

    # 销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    (23, 0, 0, 103.50),

    # 销售额 ≤ 1800
    (0, 10, 0, 100.00),
    (0, 11, 0, 104.50),
    (0, 20, 0, 170.00),
    (0, 21, 0, 174.50),

    # 销售额 > 1800
    (0, 30, 0, 220.00),
    (0, 31, 0, 224.50),
    (0, 40, 0, 280.00),
    (0, 50, 0, 340.00),

    # 组合销售
    (10, 10, 10, 220.00),
    (10, 10, 20, 260.00),
    (20, 20, 20, 440.00),
    (30, 30, 30, 660.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected