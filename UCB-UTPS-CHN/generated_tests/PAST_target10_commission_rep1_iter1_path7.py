# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1800
# 重复次数: 1, 迭代: 1
# 生成时间: 2026-04-18 15:55:14

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (-1, 10, 5, -1.0),
    (10, -1, 5, -1.0),
    (10, 10, -1, -1.0),
    # 销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 销售额 <= 1800
    (10, 10, 10, 160.00),
    (20, 0, 0, 90.00),
    (0, 20, 0, 60.00),
    (0, 0, 72, 180.00),
    # 销售额 > 1800
    (20, 20, 20, 220.00),
    (30, 0, 0, 135.00),
    (0, 30, 0, 90.00),
    (0, 0, 100, 220.00),
    # 边界值测试
    (0, 0, 40, 100.00),
    (0, 0, 41, 100.00 + 25 * 0.15),
    (0, 0, 72, 180.00),
    (0, 0, 73, 180.00 + 25 * 0.20),
    # 非整数输入（字符串）
    ("10", "10", "10", -1.0),
    ("abc", "10", "10", -1.0),
    ("10", "abc", "10", -1.0),
    ("10", "10", "abc", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected