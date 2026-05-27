# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1800
# 重复次数: 0, 迭代: 7
# 生成时间: 2026-04-26 07:13:29

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("invalid", 10, 5, -1.0),
    (10, "invalid", 5, -1.0),
    (10, 10, "invalid", -1.0),
    (10, -5, 5, -1.0),
    (-10, 10, 5, -1.0),
    (10, 10, -5, -1.0),
    # 销售额 <= 1000
    (0, 0, 0, 0.0),
    (1, 0, 0, 4.5),
    (0, 3, 0, 9.0),
    (0, 0, 4, 10.0),
    (2, 1, 1, 16.5),
    # 销售额 <= 1800
    (10, 10, 10, 220.0),
    (15, 10, 10, 272.5),
    (20, 10, 10, 325.0),
    # 销售额 > 1800
    (30, 10, 10, 460.0),
    (40, 10, 10, 600.0),
    (50, 10, 10, 740.0),
    # 边界值测试
    (0, 0, 0, 0.0),
    (22, 0, 0, 99.0),
    (23, 0, 0, 100.0 + (23*45 - 1000)*0.15),
    (40, 0, 0, 220 + (40*45 - 1800)*0.20),
    # 非整数输入（字符串）
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected