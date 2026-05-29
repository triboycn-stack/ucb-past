# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 2, 迭代: 10
# 生成时间: 2026-04-18 16:00:44

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
    (35, 10, 10, 245.00),
    (40, 10, 10, 270.00),
    (50, 10, 10, 320.00),
    
    # 边界值测试
    (0, 0, 0, 0.00),
    (22, 0, 0, 99.00),
    (23, 0, 0, 100.00),
    (40, 0, 0, 180.00),
    (41, 0, 0, 182.00),
    (40, 10, 0, 180.00),
    (40, 10, 1, 182.50),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected