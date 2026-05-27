# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales < 0)
# 重复次数: 0, 迭代: 14
# 生成时间: 2026-04-18 15:54:53

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 1, 0, 3.00),
    (0, 0, 1, 2.50),
    (2, 1, 1, 14.50),
    # 有效输入，销售额 ≤ 1800
    (10, 10, 10, 100.00 + (450 + 300 + 250 - 1000) * 0.15),
    # 有效输入，销售额 > 1800
    (20, 20, 20, 220 + (900 + 600 + 500 - 1800) * 0.20),
    # 非整数输入
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 负数输入
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 销售额为0
    (0, 0, 0, 0.00),
    # 边界值测试：销售额刚好等于1000
    (22, 0, 0, 100.00),
    # 边界值测试：销售额刚好等于1800
    (40, 0, 0, 100.00 + (1800 - 1000) * 0.15),
    # 边界值测试：销售额刚好大于1800
    (41, 0, 0, 220 + (1845 - 1800) * 0.20),
    # 非法输入（字符串）
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    # 非整数类型（浮点数）
    (1.5, 0, 0, -1.0),
    (0, 2.5, 0, -1.0),
    (0, 0, 3.5, -1.0),
    # 混合非法输入
    ("invalid", "invalid", "invalid", -1.0),
    (1, "invalid", 2, -1.0),
    ("invalid", 1, 2, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert round(result, 2) == round(expected, 2)