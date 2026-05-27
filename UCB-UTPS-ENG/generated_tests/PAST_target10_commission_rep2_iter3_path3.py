# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (locks < 0 or stocks < 0 or barrels < 0)
# 重复次数: 2, 迭代: 3
# 生成时间: 2026-04-26 07:16:52

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 4, 10.00),
    (2, 1, 1, 16.50),
    # 有效输入，销售额在 1000-1800 之间
    (10, 10, 10, 115.00),
    (15, 5, 5, 147.50),
    (5, 15, 10, 142.50),
    # 有效输入，销售额 > 1800
    (20, 20, 20, 260.00),
    (25, 25, 25, 362.50),
    (30, 30, 30, 465.00),
    # 输入验证失败（非整数）
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    # 输入验证失败（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况：销售额刚好为 1000
    (22, 0, 0, 100.00),
    # 边界情况：销售额刚好为 1800
    (40, 0, 0, 220.00),
    # 销售额为 0
    (0, 0, 0, 0.00),
    # 非法输入（字符串）
    ("abc", "def", "ghi", -1.0),
    # 非法输入（浮点数）
    (1.5, 2, 3, -1.0),
    (2, 3.5, 4, -1.0),
    (3, 4, 5.5, -1.0),
    # 非法输入（None）
    (None, 0, 0, -1.0),
    (0, None, 0, -1.0),
    (0, 0, None, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected