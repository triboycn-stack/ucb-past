# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales < 0
# 重复次数: 4, 迭代: 3
# 生成时间: 2026-04-18 16:07:19

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    # 有效输入，销售额在 1000-1800 之间
    (23, 0, 0, 100.00 + (23*45 - 1000)*0.15),
    (30, 0, 0, 100.00 + (30*45 - 1000)*0.15),
    # 有效输入，销售额 > 1800
    (40, 0, 0, 220.00 + (40*45 - 1800)*0.20),
    (50, 0, 0, 220.00 + (50*45 - 1800)*0.20),
    # 输入验证失败（非整数）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 输入验证失败（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 销售额 < 0（不可能，但测试边界检查）
    (0, 0, -100, -1.0),
    # 边界情况：销售额刚好等于 1000
    (22, 0, 0, 99.00),
    # 边界情况：销售额刚好等于 1800
    (40, 0, 0, 220.00),
    # 非法输入（字符串）
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected