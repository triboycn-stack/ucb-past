# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: locks < 0 or stocks < 0 or barrels < 0
# 重复次数: 3, 迭代: 2
# 生成时间: 2026-04-26 07:18:50

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 有效输入，销售额 ≤ 1800
    (10, 0, 0, 45.00),
    (0, 10, 0, 30.00),
    (0, 0, 72, 180.00),
    # 有效输入，销售额 > 1800
    (20, 0, 0, 90.00),
    (0, 20, 0, 60.00),
    (0, 0, 100, 220.00),
    # 输入验证：非整数
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "foo", -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况：销售额刚好为 1000
    (22, 0, 0, 100.00),
    # 边界情况：销售额刚好为 1800
    (40, 0, 0, 180.00),
    # 销售额为 0
    (0, 0, 0, 0.00),
    # 非法输入（字符串）
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected