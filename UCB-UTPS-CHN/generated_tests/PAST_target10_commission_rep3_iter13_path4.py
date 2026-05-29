# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales <= 1000)
# 重复次数: 3, 迭代: 13
# 生成时间: 2026-04-18 16:06:09

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("invalid", 10, 20, -1.0),
    (10, "invalid", 20, -1.0),
    (10, 10, "invalid", -1.0),
    (10, -5, 20, -1.0),
    (-5, 10, 20, -1.0),
    (10, 10, -5, -1.0),
    # 销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 销售额 ≤ 1800
    (10, 10, 0, 100.00),
    (5, 15, 0, 100.00),
    (0, 0, 60, 100.00),
    (0, 0, 61, 100.15),
    # 销售额 > 1800
    (0, 0, 72, 124.00),
    (10, 10, 10, 175.00),
    (20, 20, 20, 220.00),
    (30, 30, 30, 340.00),
    # 边界值测试
    (0, 0, 40, 100.00),
    (0, 0, 41, 100.15),
    (0, 0, 72, 124.00),
    (0, 0, 73, 124.20),
    # 非整数输入（字符串）
    ("10", "10", "10", -1.0),
    ("hello", "world", "test", -1.0),
    # 浮点数输入（应返回-1.0）
    (10.5, 20, 30, -1.0),
    (10, 20.5, 30, -1.0),
    (10, 20, 30.5, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected