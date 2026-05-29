# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1000
# 重复次数: 3, 迭代: 9
# 生成时间: 2026-04-18 16:05:15

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    (0, 0, -1, -1.0),
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    # 销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    (2, 1, 0, 13.50),
    # 销售额 <= 1800
    (0, 0, 41, 102.50),
    (0, 5, 0, 22.50),
    (3, 2, 0, 22.50),
    (0, 0, 60, 150.00),
    # 销售额 > 1800
    (0, 0, 73, 220.00),
    (0, 0, 74, 222.00),
    (0, 0, 90, 260.00),
    (10, 10, 10, 220.00),
    # 边界值测试
    (0, 0, 0, 0.00),
    (0, 0, 40, 100.00),
    (0, 0, 41, 102.50),
    (0, 0, 72, 218.00),
    (0, 0, 73, 220.00),
    # 非整数输入（应返回-1.0）
    (1.5, 0, 0, -1.0),
    (0, 2.5, 0, -1.0),
    (0, 0, 3.5, -1.0),
    # 大数值测试
    (1000, 0, 0, 45000.00),
    (0, 600, 0, 18000.00),
    (0, 0, 720, 18000.00),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected