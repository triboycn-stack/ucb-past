# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int)))
# 重复次数: 1, 迭代: 8
# 生成时间: 2026-04-18 15:56:55

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 有效输入，销售额在 1000-1800 之间
    (10, 10, 10, 100.00 + (450 + 300 + 250 - 1000) * 0.15),
    # 有效输入，销售额 > 1800
    (20, 20, 20, 220 + (900 + 600 + 500 - 1800) * 0.20),
    # 边界值测试
    (0, 0, 0, 0.00),
    (22, 0, 0, 99.00),
    (0, 30, 0, 90.00),
    (0, 0, 72, 180.00),
    # 输入验证：非整数类型
    ("123", 0, 0, -1.0),
    (123.0, 0, 0, -1.0),
    (None, 0, 0, -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 混合非法输入
    ("abc", "def", "ghi", -1.0),
    (123, "xyz", 456, -1.0),
    (123, 456, "789", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected