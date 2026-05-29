# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 0, 迭代: 10
# 生成时间: 2026-04-18 15:53:49

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (10.5, 10, 5, -1.0),
    (10, 10.5, 5, -1.0),
    (10, 10, 5.5, -1.0),
    (10, -5, 5, -1.0),
    (-10, 10, 5, -1.0),
    (10, 10, -5, -1.0),
    # 销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 2, 0, 6.00),
    (0, 0, 40, 100.00),
    # 销售额 ≤ 1800
    (10, 10, 0, 100.00),
    (0, 30, 0, 100.00),
    (0, 0, 72, 100.00),
    (10, 0, 10, 100.00),
    (5, 10, 10, 100.00),
    # 销售额 > 1800
    (10, 10, 10, 220.00),
    (20, 20, 20, 220.00),
    (0, 0, 100, 220.00),
    (10, 10, 20, 220.00),
    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 1, 25.00),
    (0, 0, 40, 100.00),
    (0, 0, 72, 100.00),
    (0, 0, 73, 100.00 + 25 * 0.20),
    (0, 0, 100, 220.00),
    (0, 0, 101, 220.00 + 25 * 0.20),
    # 复杂组合测试
    (10, 20, 30, 220.00),
    (5, 15, 25, 220.00),
    (0, 10, 50, 220.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected