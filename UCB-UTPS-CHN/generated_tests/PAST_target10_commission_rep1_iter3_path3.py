# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (locks < 0 or stocks < 0 or barrels < 0)
# 重复次数: 1, 迭代: 3
# 生成时间: 2026-04-26 07:14:39

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 有效输入，销售额在 1000-1800 之间
    (10, 10, 10, 145.00),
    (20, 0, 0, 190.00),
    (0, 20, 0, 190.00),
    (0, 0, 72, 190.00),
    # 有效输入，销售额 > 1800
    (50, 0, 0, 320.00),
    (0, 60, 0, 320.00),
    (0, 0, 100, 320.00),
    (10, 10, 20, 280.00),
    # 边界值测试
    (0, 0, 0, 0.00),
    (22, 0, 0, 100.00),
    (23, 0, 0, 103.50),
    (40, 0, 0, 220.00),
    (41, 0, 0, 220.00 + 0.20 * 1, 220.20),
    # 非法输入（类型错误）
    ("hello", 0, 0, -1.0),
    (1, "world", 0, -1.0),
    (1, 0, "test", -1.0),
    # 非法输入（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 非法输入（非整数）
    (1.5, 0, 0, -1.0),
    (0, 2.5, 0, -1.0),
    (0, 0, 3.5, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected