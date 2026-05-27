# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1800
# 重复次数: 1, 迭代: 7
# 生成时间: 2026-04-26 07:15:18

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("invalid", 10, 20, -1.0),
    (10, "invalid", 20, -1.0),
    (10, 20, "invalid", -1.0),
    (10.5, 20, 30, -1.0),
    (10, 20.5, 30, -1.0),
    (10, 20, 30.5, -1.0),
    (-1, 10, 20, -1.0),
    (10, -1, 20, -1.0),
    (10, 20, -1, -1.0),
    
    # 销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 0, 13.50),
    
    # 销售额 <= 1800
    (10, 10, 10, 160.00),
    (5, 5, 10, 117.50),
    (0, 20, 20, 150.00),
    (15, 10, 0, 157.50),
    
    # 销售额 > 1800
    (20, 20, 20, 280.00),
    (10, 30, 20, 250.00),
    (0, 40, 30, 280.00),
    (25, 25, 25, 332.50),
    
    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 40, 100.00),
    (0, 0, 41, 102.50),
    (0, 0, 72, 180.00),
    (0, 0, 73, 182.50),
    (0, 0, 100, 220.00),
    (0, 0, 101, 222.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected