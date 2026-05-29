# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales < 0
# 重复次数: 2, 迭代: 14
# 生成时间: 2026-04-18 16:03:14

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (2, 0, 0, 9.00),
    (0, 1, 0, 3.00),
    (0, 0, 4, 2.00),
    # 有效输入，销售额在 1000-1800 之间
    (10, 10, 10, 145.00),
    (15, 15, 15, 227.50),
    (20, 20, 20, 310.00),
    # 有效输入，销售额 > 1800
    (30, 30, 30, 460.00),
    (40, 40, 40, 620.00),
    (50, 50, 50, 780.00),
    # 输入验证：非整数
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 销售额 < 0（理论上不可能，但测试边界条件）
    (0, 0, -100, -1.0),
    # 边界情况：销售额刚好为 1000
    (22, 0, 0, 100.00),
    # 边界情况：销售额刚好为 1800
    (40, 0, 0, 220.00),
    # 销售额为 0
    (0, 0, 0, 0.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected