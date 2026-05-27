# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1000
# 重复次数: 2, 迭代: 6
# 生成时间: 2026-04-26 07:17:37

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    (0, 0, -1, -1.0),
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -2, -1.0),

    # 销售额 <= 1000 的情况
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 3, 22.50),

    # 销售额 <= 1800 的情况
    (10, 0, 0, 45.00),
    (0, 6, 0, 18.00),
    (0, 0, 72, 180.00),
    (5, 5, 5, 52.50),

    # 销售额 > 1800 的情况
    (10, 10, 10, 100.00),
    (20, 0, 0, 90.00),
    (0, 10, 10, 60.00),
    (0, 0, 100, 220.00),
    (15, 15, 15, 112.50),

    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 1, 25.00),
    (0, 0, 40, 100.00),
    (0, 0, 72, 180.00),
    (0, 0, 73, 220.00),
    (0, 0, 100, 220.00),
    (0, 0, 101, 220.00 + 25.00 * 0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected