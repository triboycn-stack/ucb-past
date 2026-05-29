# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 4, 迭代: 11
# 生成时间: 2026-04-18 16:09:43

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
    
    # 销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 2, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 3, 100.00),
    
    # 销售额 ≤ 1800
    (10, 10, 10, 100.00 + (450 + 300 + 250 - 1000) * 0.15),
    (10, 10, 15, 100.00 + (450 + 300 + 375 - 1000) * 0.15),
    (0, 0, 60, 100.00 + (1500 - 1000) * 0.15),
    
    # 销售额 > 1800
    (10, 10, 20, 220.00 + (450 + 300 + 500 - 1800) * 0.20),
    (0, 0, 100, 220.00 + (2500 - 1800) * 0.20),
    (5, 5, 50, 220.00 + (225 + 150 + 1250 - 1800) * 0.20),
    
    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 40, 100.00),
    (0, 0, 41, 100.00 + (1025 - 1000) * 0.15),
    (0, 0, 72, 220.00 + (1800 - 1800) * 0.20),
    (0, 0, 73, 220.00 + (1825 - 1800) * 0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert round(result, 2) == round(expected, 2)