# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1000
# 重复次数: 3, 迭代: 6
# 生成时间: 2026-04-26 07:20:44

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("invalid", 10, 5, -1.0),
    (10, "invalid", 5, -1.0),
    (10, 10, "invalid", -1.0),
    (-1, 10, 5, -1.0),
    (10, -1, 5, -1.0),
    (10, 10, -1, -1.0),
    # 销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 销售额 <= 1800
    (0, 0, 41, 102.00),
    (10, 10, 10, 165.00),
    (0, 20, 20, 180.00),
    # 销售额 > 1800
    (0, 20, 21, 182.00),
    (10, 10, 20, 220.00),
    (0, 0, 100, 220.00),
    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 40, 100.00),
    (0, 0, 41, 102.00),
    (0, 0, 72, 220.00),
    (0, 0, 73, 222.00),
    # 非整数输入（字符串）
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected