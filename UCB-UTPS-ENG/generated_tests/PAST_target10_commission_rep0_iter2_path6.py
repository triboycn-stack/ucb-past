# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1000
# 重复次数: 0, 迭代: 2
# 生成时间: 2026-04-18 15:51:56

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    (0, 0, -1, -1.0),
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),

    # 销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 4, 10.00),
    (2, 1, 1, 14.50),

    # 销售额 <= 1800
    (10, 0, 0, 45.00),
    (0, 10, 0, 30.00),
    (0, 0, 12, 30.00),
    (5, 5, 5, 47.50),
    (15, 0, 0, 67.50),

    # 销售额 > 1800
    (20, 0, 0, 90.00),
    (0, 20, 0, 60.00),
    (0, 0, 24, 60.00),
    (10, 10, 10, 85.00),
    (30, 0, 0, 130.00),

    # 边界值测试
    (0, 0, 0, 0.00),
    (22, 0, 0, 99.00),
    (23, 0, 0, 100.50),
    (40, 0, 0, 160.00),
    (41, 0, 0, 162.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected