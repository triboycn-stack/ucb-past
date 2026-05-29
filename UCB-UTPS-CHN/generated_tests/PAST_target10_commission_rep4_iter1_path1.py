# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 4, 迭代: 1
# 生成时间: 2026-04-26 07:21:41

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
    (0, 2, 0, 6.00),
    (0, 0, 4, 5.00),
    (2, 1, 1, 13.50),
    
    # 销售额 ≤ 1800 的情况
    (10, 10, 10, 100.00),
    (15, 10, 10, 127.50),
    (20, 10, 10, 155.00),
    (25, 10, 10, 182.50),
    
    # 销售额 > 1800 的情况
    (30, 10, 10, 220.00),
    (35, 10, 10, 240.00),
    (40, 10, 10, 260.00),
    (50, 10, 10, 300.00),
    
    # 边界值测试
    (0, 0, 0, 0.00),
    (22, 0, 0, 99.00),
    (23, 0, 0, 100.00 + (23*45 - 1000)*0.15),
    (40, 0, 0, 220.00 + (40*45 - 1800)*0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected