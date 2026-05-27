# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 4, 迭代: 2
# 生成时间: 2026-04-18 16:07:09

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 1, 0, 3.00),
    (0, 0, 1, 2.50),
    (2, 1, 1, 14.50),
    # 有效输入，销售额 ≤ 1800
    (10, 10, 10, 100.00),
    (15, 10, 10, 145.00),
    (20, 10, 10, 190.00),
    # 有效输入，销售额 > 1800
    (30, 10, 10, 260.00),
    (40, 10, 10, 340.00),
    (50, 10, 10, 420.00),
    # 输入验证：非整数
    ("hello", 1, 1, -1.0),
    (1, "hello", 1, -1.0),
    (1, 1, "hello", -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况：销售额为 1000
    (22, 0, 0, 100.00),
    # 边界情况：销售额为 1800
    (40, 0, 0, 180.00),
    # 销售额刚好超过 1800
    (41, 0, 0, 220.00),
    # 非法输入（字符串）
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected