# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales < 0
# 重复次数: 4, 迭代: 9
# 生成时间: 2026-04-26 07:23:27

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    # 有效输入，销售额 ≤ 1800
    (23, 0, 0, 100.00 + (23*45 - 1000)*0.15),
    (40, 0, 0, 100.00 + (40*45 - 1000)*0.15),
    # 有效输入，销售额 > 1800
    (41, 0, 0, 220.00 + (41*45 - 1800)*0.20),
    (100, 0, 0, 220.00 + (100*45 - 1800)*0.20),
    # 输入验证：非整数
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 销售额 < 0（不可能，但测试边界检查）
    (0, 0, -100, -1.0),
    # 边界情况：销售额刚好为1000
    (22, 0, 0, 99.00),
    # 边界情况：销售额刚好为1800
    (40, 0, 0, 100.00 + (1800 - 1000)*0.15),
    # 边界情况：销售额刚好为1801
    (40, 0, 1, 220.00 + (1801 - 1800)*0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected