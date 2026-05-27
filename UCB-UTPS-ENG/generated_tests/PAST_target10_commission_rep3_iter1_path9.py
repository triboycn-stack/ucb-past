# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales < 0
# 重复次数: 3, 迭代: 1
# 生成时间: 2026-04-18 16:03:36

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (10, 10, -5, -1.0),
    (-5, 10, 10, -1.0),
    (10, -5, 10, -1.0),
    (10.5, 10, 10, -1.0),
    (10, 10.5, 10, -1.0),
    (10, 10, 10.5, -1.0),

    # 销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 1, 14.50),

    # 销售额 ≤ 1800
    (10, 10, 10, 100.00 + (450 + 300 + 250 - 1000) * 0.15),
    (10, 10, 20, 100.00 + (450 + 300 + 500 - 1000) * 0.15),
    (0, 0, 60, 100.00 + (1500 - 1000) * 0.15),

    # 销售额 > 1800
    (10, 10, 30, 220.00 + (450 + 300 + 750 - 1800) * 0.20),
    (0, 0, 100, 220.00 + (2500 - 1800) * 0.20),
    (10, 20, 40, 220.00 + (450 + 600 + 1000 - 1800) * 0.20),

    # 边界检查（sales < 0）
    (0, 0, -1, -1.0),
    (-1, 0, 0, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected