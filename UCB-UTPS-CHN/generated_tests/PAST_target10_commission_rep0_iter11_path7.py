# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1800
# 重复次数: 0, 迭代: 11
# 生成时间: 2026-04-18 15:53:59

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("hello", 10, 20, -1.0),
    (10, "world", 20, -1.0),
    (10, 20, "foo", -1.0),
    (10, -5, 20, -1.0),
    (-3, 10, 20, -1.0),
    (10, 20, -1, -1.0),

    # 销售额 <= 1000 的情况
    (0, 0, 0, 0.0),
    (1, 0, 0, 4.5),
    (0, 3, 0, 9.0),
    (0, 0, 40, 100.0),
    (2, 1, 1, 14.5),

    # 销售额在 1000 和 1800 之间的情况
    (10, 10, 10, 160.0),
    (15, 10, 10, 205.0),
    (5, 15, 10, 175.0),
    (0, 20, 20, 170.0),

    # 销售额 > 1800 的情况
    (20, 20, 20, 260.0),
    (30, 30, 30, 460.0),
    (10, 30, 20, 300.0),
    (0, 40, 30, 370.0),

    # 边界值测试
    (0, 0, 40, 100.0),
    (0, 0, 41, 102.5),
    (0, 0, 72, 180.0),
    (0, 0, 73, 182.0),
    (0, 0, 100, 220.0),
    (0, 0, 101, 222.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected