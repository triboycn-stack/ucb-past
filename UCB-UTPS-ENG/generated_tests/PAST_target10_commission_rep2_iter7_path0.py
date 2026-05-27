# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 2, 迭代: 7
# 生成时间: 2026-04-18 16:00:06

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
    (10, 10, 10, 100.00 + (450 + 300 + 250 - 1000) * 0.15),
    # 有效输入，销售额 > 1800
    (20, 20, 20, 220 + (900 + 600 + 500 - 1800) * 0.20),
    # 输入验证：非整数类型
    ("hello", 1, 1, -1.0),
    (1, "world", 1, -1.0),
    (1, 1, "foo", -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 输入验证：混合非法输入
    ("invalid", -1, 0, -1.0),
    # 边界条件：刚好等于 1000
    (22, 0, 0, 100.00),
    # 边界条件：刚好等于 1800
    (40, 0, 0, 220.00),
    # 边界条件：刚好超过 1800
    (41, 0, 0, 220.00 + (41*45 - 1800)*0.20),
    # 非法输入（字符串）
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
    # 空值（虽然参数是 int 类型，但这里模拟错误输入）
    (None, None, None, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected