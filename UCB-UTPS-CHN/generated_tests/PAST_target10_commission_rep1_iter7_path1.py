# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 1, 迭代: 7
# 生成时间: 2026-04-18 15:56:47

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
    (1.5, 2, 3, -1.0),
    (1, "invalid", 3, -1.0),
    (1, 2, None, -1.0),
    (1, 2, 3.5, -1.0),

    # 锁销售数量为负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),

    # 销售额 ≤ 1000
    (0, 0, 0, 0.0),
    (1, 0, 0, 4.5),
    (0, 3, 0, 9.0),
    (0, 0, 40, 100.0),
    (2, 1, 0, 13.5),

    # 销售额 ≤ 1800
    (0, 0, 41, 102.5),
    (1, 2, 10, 100.0 + (45 + 60 + 250 - 1000) * 0.15),
    (0, 5, 20, 100.0 + (150 + 500 - 1000) * 0.15),

    # 销售额 > 1800
    (0, 0, 73, 220 + (1825 - 1800) * 0.20),
    (2, 3, 30, 220 + (90 + 90 + 750 - 1800) * 0.20),
    (10, 10, 10, 220 + (450 + 300 + 250 - 1800) * 0.20),

    # 边界值测试
    (0, 0, 0, 0.0),
    (0, 0, 40, 100.0),
    (0, 0, 41, 102.5),
    (0, 0, 72, 220.0),
    (0, 0, 73, 220.0 + 5.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected