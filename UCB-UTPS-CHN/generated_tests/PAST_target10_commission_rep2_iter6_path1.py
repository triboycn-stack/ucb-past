# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 2, 迭代: 6
# 生成时间: 2026-04-18 15:59:55

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (10.5, 10, 5, -1.0),
    (10, 10.5, 5, -1.0),
    (10, 10, 10.5, -1.0),
    (-1, 10, 5, -1.0),
    (10, -1, 5, -1.0),
    (10, 10, -1, -1.0),
    
    # 销售额 ≤ 1000 的情况
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 0, 13.50),
    
    # 销售额 ≤ 1800 的情况
    (10, 10, 10, 175.00),
    (5, 5, 10, 122.50),
    (0, 10, 20, 130.00),
    (10, 0, 20, 145.00),
    
    # 销售额 > 1800 的情况
    (20, 20, 20, 260.00),
    (15, 15, 20, 242.50),
    (10, 10, 30, 235.00),
    (0, 0, 100, 220.00),
    
    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 1, 25.00),
    (0, 0, 40, 100.00),
    (0, 0, 72, 180.00),
    (0, 0, 73, 180.00 + 25 * 0.20),
    (0, 0, 100, 220.00),
    (0, 0, 101, 220.00 + 25 * 0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected