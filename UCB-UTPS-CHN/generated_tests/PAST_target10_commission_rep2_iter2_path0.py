# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 2, 迭代: 2
# 生成时间: 2026-04-18 15:58:59

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
    (22, 2, 0, 108.00),
    (22, 6, 0, 123.00),
    (22, 10, 0, 138.00),
    
    # 有效输入，销售额 > 1800
    (40, 0, 0, 220.00),
    (41, 0, 0, 228.00),
    (50, 0, 0, 300.00),
    (60, 0, 0, 400.00),
    
    # 输入验证：非整数类型
    ("123", 0, 0, -1.0),
    (123, "abc", 0, -1.0),
    (123, 456, "789", -1.0),
    
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    
    # 输入验证：混合非法输入
    ("abc", "def", "ghi", -1.0),
    (-1, "abc", 0, -1.0),
    
    # 边界情况：销售额刚好为 1000
    (22, 1, 0, 103.50),
    (22, 0, 2, 100.00),
    
    # 边界情况：销售额刚好为 1800
    (40, 0, 0, 220.00),
    (36, 2, 0, 1800.00),
    
    # 非法输入（字符串但可转换为整数）
    ("123", "456", "789", -1.0),
    ("  123  ", "  456  ", "  789  ", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected