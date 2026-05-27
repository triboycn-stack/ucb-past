# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales <= 1800)
# 重复次数: 0, 迭代: 5
# 生成时间: 2026-04-26 07:13:00

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 20, -1.0),
    (10, "  hello\n    world", 20, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (10.5, 10, 20, -1.0),
    (10, 10.5, 20, -1.0),
    (10, 10, 10.5, -1.0),
    (-1, 10, 20, -1.0),
    (10, -1, 20, -1.0),
    (10, 10, -1, -1.0),
    
    # 销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 3, 22.50),
    
    # 销售额 ≤ 1800
    (0, 0, 41, 102.50),
    (0, 10, 20, 130.00),
    (5, 5, 10, 127.50),
    
    # 销售额 > 1800
    (0, 0, 100, 220.00),
    (0, 20, 30, 265.00),
    (10, 10, 30, 310.00),
    (20, 20, 20, 340.00),
    
    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 40, 100.00),
    (0, 0, 41, 102.50),
    (0, 0, 72, 220.00),
    (0, 0, 73, 222.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected