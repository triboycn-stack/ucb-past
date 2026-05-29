# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (locks < 0 or stocks < 0 or barrels < 0)
# 重复次数: 1, 迭代: 10
# 生成时间: 2026-04-26 07:16:01

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
    (15, 10, 10, 142.50),
    (20, 10, 10, 190.00),
    # 有效输入，销售额 > 1800
    (30, 10, 10, 260.00),
    (40, 10, 10, 340.00),
    (50, 10, 10, 420.00),
    # 边界情况
    (0, 0, 0, 0.00),
    (22, 22, 22, 220.00),
    (23, 23, 23, 220.00 + (23*45 + 23*30 + 23*25 - 1800)*0.20),
    # 非整数输入
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    # 负数输入
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 销售额为负数（不可能，但测试边界）
    (0, 0, 1000000, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected