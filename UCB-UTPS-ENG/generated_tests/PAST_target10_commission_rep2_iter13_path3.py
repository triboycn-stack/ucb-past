# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (locks < 0 or stocks < 0 or barrels < 0)
# 重复次数: 2, 迭代: 13
# 生成时间: 2026-04-18 16:03:04

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 4, 10.00),
    (2, 1, 1, 16.50),
    # 有效输入，销售额在 1000-1800 之间
    (10, 10, 10, 145.00),
    (15, 5, 5, 175.00),
    (20, 0, 0, 180.00),
    # 有效输入，销售额 > 1800
    (30, 0, 0, 220.00),
    (25, 10, 5, 257.50),
    (10, 20, 10, 265.00),
    # 边界情况：销售额刚好为 1000
    (22, 0, 0, 100.00),
    # 边界情况：销售额刚好为 1800
    (40, 0, 0, 220.00),
    # 非整数输入（非法）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 负数输入（非法）
    (-1, 0, 0, -1.0),
    (0, -5, 0, -1.0),
    (0, 0, -3, -1.0),
    # 非整数类型输入（非法）
    (1.5, 0, 0, -1.0),
    (0, 2.5, 0, -1.0),
    (0, 0, 3.5, -1.0),
    # 字符串输入（非法）
    ("10", "20", "30", -1.0),
    # 空字符串输入（非法）
    ("", "", "", -1.0),
    # 混合非法输入
    ("invalid", -1, 0, -1.0),
    (10, "invalid", -5, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected