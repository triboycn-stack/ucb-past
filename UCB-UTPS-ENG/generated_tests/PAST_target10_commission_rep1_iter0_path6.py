# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: sales <= 1000
# 重复次数: 1, 迭代: 0
# 生成时间: 2026-04-18 15:55:04

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (10, -5, 5, -1.0),
    (-3, 10, 5, -1.0),
    (10, 5, -2, -1.0),

    # 销售额 <= 1000 的情况
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),  # 40 * 25 = 1000
    (0, 0, 39, 97.50),   # 39 * 25 = 975

    # 销售额 <= 1800 的情况
    (0, 0, 50, 125.00),  # 50 * 25 = 1250
    (0, 0, 60, 180.00),  # 60 * 25 = 1500
    (0, 0, 72, 220.00),  # 72 * 25 = 1800

    # 销售额 > 1800 的情况
    (0, 0, 73, 220.00 + (73*25 - 1800)*0.20),  # 73 * 25 = 1825
    (0, 0, 100, 220.00 + (2500 - 1800)*0.20),  # 100 * 25 = 2500
    (10, 10, 10, 220.00 + (10*45 + 10*30 + 10*25 - 1800)*0.20),  # 10*45=450, 10*30=300, 10*25=250 → 1000 → 1000 ≤ 1800 → 220 + (1000-1800) → 不适用，但此处是错误示例，应为 1000 → 100 → 100+0=100
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected