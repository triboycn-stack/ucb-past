# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales < 0)
# 重复次数: 3, 迭代: 8
# 生成时间: 2026-04-26 07:21:05

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    (23, 0, 0, 103.50),
    
    # 有效输入，销售额在 1000-1800 之间
    (22, 1, 0, 103.50),
    (10, 10, 10, 165.00),
    (15, 15, 15, 217.50),
    
    # 有效输入，销售额 > 1800
    (40, 0, 0, 220.00),
    (30, 10, 0, 220.00),
    (20, 20, 20, 260.00),
    (50, 50, 50, 490.00),
    
    # 输入验证：非整数类型
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    
    # 边界检查：销售额 < 0（理论上不可能，但测试逻辑）
    (0, 0, -10, -1.0),
    
    # 非法输入组合
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
    (-1, -1, -1, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected