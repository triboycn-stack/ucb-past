# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: locks < 0 or stocks < 0 or barrels < 0
# 重复次数: 1, 迭代: 12
# 生成时间: 2026-04-18 15:57:59

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    (0, 0, 0, -1.0),
    (0, 0, -1, -1.0),
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -2, -1.0),

    # 销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 4, 10.00),
    (2, 1, 1, 16.50),

    # 销售额 ≤ 1800
    (10, 0, 0, 45.00),
    (0, 10, 0, 30.00),
    (0, 0, 12, 30.00),
    (5, 5, 5, 52.50),
    (10, 5, 5, 75.00),

    # 销售额 > 1800
    (20, 0, 0, 110.00),
    (0, 20, 0, 90.00),
    (0, 0, 24, 60.00),
    (10, 10, 10, 115.00),
    (15, 15, 15, 167.50),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected