# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 3, 迭代: 10
# 生成时间: 2026-04-18 16:05:37

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    # 有效输入，销售额在 1000-1800 之间
    (23, 0, 0, 100.00 + (23*45 - 1000)*0.15),
    (20, 10, 0, 100.00 + (20*45 + 10*30 - 1000)*0.15),
    # 有效输入，销售额 > 1800
    (40, 0, 0, 220.00 + (40*45 - 1800)*0.20),
    (30, 10, 5, 220.00 + (30*45 + 10*30 + 5*25 - 1800)*0.20),
    # 无效输入：非整数
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 无效输入：负数
    (-1, 0, 0, -1.0),
    (0, -5, 0, -1.0),
    (0, 0, -3, -1.0),
    # 无效输入：混合类型
    ("123", "456", "789", -1.0),
    # 边界情况：刚好等于 1000
    (22, 0, 0, 99.00),
    # 边界情况：刚好等于 1800
    (40, 0, 0, 220.00),
    # 销售额为 0
    (0, 0, 0, 0.00),
    # 销售额为 1000
    (22, 0, 0, 99.00),
    # 销售额为 1800
    (40, 0, 0, 220.00),
    # 销售额为 1001
    (23, 0, 0, 100.00 + (23*45 - 1000)*0.15),
    # 销售额为 1799
    (39, 0, 0, 100.00 + (39*45 - 1000)*0.15),
    # 销售额为 1801
    (40, 0, 0, 220.00 + (40*45 - 1800)*0.20),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected