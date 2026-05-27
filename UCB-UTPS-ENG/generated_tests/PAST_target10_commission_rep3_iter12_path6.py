# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1000
# 重复次数: 3, 迭代: 12
# 生成时间: 2026-04-18 16:05:59

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 1, 0, 3.00),
    (0, 0, 1, 2.50),
    (2, 1, 1, 14.50),
    # 有效输入，销售额 <= 1800
    (10, 10, 10, 100.00),
    (15, 10, 10, 122.50),
    # 有效输入，销售额 > 1800
    (20, 20, 20, 220.00),
    (30, 30, 30, 340.00),
    # 无效输入（非整数）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 无效输入（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况：销售额刚好为1000
    (22, 0, 0, 100.00),
    # 边界情况：销售额刚好为1800
    (40, 0, 0, 220.00),
    # 非法输入（字符串）
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected