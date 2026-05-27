# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales <= 1800)
# 重复次数: 2, 迭代: 8
# 生成时间: 2026-04-18 16:00:24

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (2, 0, 0, 9.00),
    (0, 3, 0, 9.00),
    (0, 0, 4, 10.00),
    (1, 1, 1, 10.00),
    # 有效输入，销售额 <= 1800
    (10, 0, 0, 45.00),
    (0, 10, 0, 30.00),
    (0, 0, 12, 30.00),
    (5, 5, 5, 45.00 + 15.00 + 12.50 = 72.50),
    # 有效输入，销售额 > 1800
    (20, 0, 0, 220 + (900 * 0.20) = 380.00),
    (0, 20, 0, 220 + (600 * 0.20) = 340.00),
    (0, 0, 24, 220 + (400 * 0.20) = 300.00),
    (10, 10, 10, 450 + 300 + 250 = 1000 → 100 + 100 * 0.15 = 115.00),
    # 输入验证失败（非整数）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 输入验证失败（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况（销售额刚好为1000）
    (22, 0, 0, 100.00),
    # 边界情况（销售额刚好为1800）
    (40, 0, 0, 220.00),
    # 销售额为0
    (0, 0, 0, 0.00),
    # 非法输入（字符串）
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected