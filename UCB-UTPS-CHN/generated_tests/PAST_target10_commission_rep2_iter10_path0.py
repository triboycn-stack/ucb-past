# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 2, 迭代: 10
# 生成时间: 2026-04-26 07:18:18

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
    (10, 0, 0, 45.00),
    (0, 10, 0, 30.00),
    (0, 0, 10, 25.00),
    (5, 5, 5, 57.50),
    # 有效输入，销售额 > 1800
    (20, 0, 0, 90.00),
    (0, 20, 0, 60.00),
    (0, 0, 20, 50.00),
    (10, 10, 10, 145.00),
    # 输入验证失败（非整数）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 输入验证失败（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况（销售额刚好为1000）
    (22, 0, 0, 100.00),
    # 边界情况（销售额刚好为1800）
    (40, 0, 0, 180.00),
    # 非法输入（混合类型）
    ("123", "456", "789", -1.0),
    # 空值（应视为0）
    (None, None, None, -1.0),
    # 大数值（测试边界检查）
    (1000000, 0, 0, 200000.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected