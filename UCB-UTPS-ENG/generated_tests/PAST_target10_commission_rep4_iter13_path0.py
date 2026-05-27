# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 4, 迭代: 13
# 生成时间: 2026-04-18 16:10:05

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 ≤ 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (2, 0, 0, 9.00),
    (0, 3, 0, 9.00),
    (0, 0, 4, 10.00),
    (1, 1, 1, 10.00),
    # 有效输入，销售额 ≤ 1800
    (10, 0, 0, 45.00),
    (0, 10, 0, 30.00),
    (0, 0, 12, 30.00),
    (5, 5, 5, 52.50),
    # 有效输入，销售额 > 1800
    (20, 0, 0, 90.00),
    (0, 20, 0, 60.00),
    (0, 0, 24, 60.00),
    (10, 10, 10, 115.00),
    # 边界情况
    (0, 0, 0, 0.00),
    (1, 1, 1, 10.00),
    (22, 0, 0, 99.00),
    (0, 26, 0, 78.00),
    (0, 0, 36, 90.00),
    # 输入验证：非整数类型
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    (None, 0, 0, -1.0),
    (0, None, 0, -1.0),
    (0, 0, None, -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 输入验证：混合非法输入
    ("invalid", -1, 0, -1.0),
    (1, "invalid", -1, -1.0),
    (-1, "invalid", "invalid", -1.0),
    # 浮点数输入（应视为非法）
    (1.0, 0, 0, -1.0),
    (0, 2.5, 0, -1.0),
    (0, 0, 3.0, -1.0),
    # 非字符串输入（但为整数类型）
    (1, 2, 3, 22.50),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected