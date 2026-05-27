# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales < 0
# 重复次数: 0, 迭代: 9
# 生成时间: 2026-04-26 07:13:47

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
    # 有效输入，销售额在 1000-1800 之间
    (10, 10, 10, 100.00),
    (15, 15, 15, 172.50),
    (20, 20, 20, 245.00),
    # 有效输入，销售额 > 1800
    (30, 30, 30, 340.00),
    (40, 40, 40, 460.00),
    (50, 50, 50, 580.00),
    # 输入验证：非整数
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 销售额 < 0（通过负数销售数量触发）
    (-1, -1, -1, -1.0),
    # 边界条件：销售额刚好为 1000
    (22, 0, 0, 100.00),
    # 边界条件：销售额刚好为 1800
    (40, 0, 0, 180.00),
    # 销售额为 0
    (0, 0, 0, 0.00),
    # 非法输入：字符串类型
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected