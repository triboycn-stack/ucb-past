# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 2, 迭代: 1
# 生成时间: 2026-04-18 15:58:49

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 有效输入，销售额 ≤ 1800
    (2, 1, 0, 12.75),
    (0, 6, 0, 18.00),
    (0, 0, 72, 180.00),
    # 有效输入，销售额 > 1800
    (3, 2, 0, 24.00),
    (0, 8, 0, 24.00),
    (0, 0, 100, 220.00),
    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 1, 25.00),
    (0, 0, 40, 100.00),
    (0, 0, 72, 180.00),
    (0, 0, 100, 220.00),
    # 非整数输入（应返回 -1.0）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 负数输入（应返回 -1.0）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 混合非法输入
    ("invalid", "invalid", "invalid", -1.0),
    (1, "invalid", 2, -1.0),
    (1, 2, "invalid", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected