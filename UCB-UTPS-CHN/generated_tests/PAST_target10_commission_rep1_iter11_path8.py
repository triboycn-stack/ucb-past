# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales < 0)
# 重复次数: 1, 迭代: 11
# 生成时间: 2026-04-18 15:57:40

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    # 有效输入，销售额在 1000-1800 之间
    (23, 0, 0, 100.00 + (1035 - 1000) * 0.15),
    (30, 0, 0, 100.00 + (1350 - 1000) * 0.15),
    # 有效输入，销售额 > 1800
    (40, 0, 0, 220 + (1800 - 1800) * 0.20),
    (41, 0, 0, 220 + (1845 - 1800) * 0.20),
    # 无效输入（非整数）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 无效输入（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况：销售额刚好为 1000
    (22, 1, 0, 1000.00),
    # 边界情况：销售额刚好为 1800
    (40, 0, 0, 1800.00),
    # 销售额为 0
    (0, 0, 0, 0.00),
    # 非法输入（字符串）
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
    # 非法输入（浮点数）
    (1.5, 0, 0, -1.0),
    (0, 2.5, 0, -1.0),
    (0, 0, 3.5, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert round(result, 2) == round(expected, 2)