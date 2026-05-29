# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: locks < 0 or stocks < 0 or barrels < 0
# 重复次数: 1, 迭代: 14
# 生成时间: 2026-04-18 15:58:30

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
    (10, 10, 10, -1.0),  # 非整数输入（但此处为整数，所以不触发）

    # 销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (2, 0, 0, 9.00),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (1, 1, 1, 10.00),

    # 销售额 ≤ 1800
    (10, 10, 10, 160.00),
    (15, 10, 10, 205.00),
    (20, 10, 10, 250.00),
    (0, 20, 20, 160.00),
    (5, 10, 20, 175.00),

    # 销售额 > 1800
    (30, 10, 10, 300.00),
    (40, 10, 10, 380.00),
    (50, 10, 10, 460.00),
    (0, 30, 30, 220.00),
    (10, 20, 30, 340.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected