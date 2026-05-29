# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales <= 1800)
# 重复次数: 2, 迭代: 5
# 生成时间: 2026-04-26 07:17:20

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 有效输入，销售额 <= 1800
    (10, 0, 0, 45.00),
    (0, 6, 0, 18.00),
    (0, 0, 72, 180.00),
    (5, 5, 5, 45.00 + 15.00 + 12.50 = 72.50),
    # 有效输入，销售额 > 1800
    (10, 10, 10, 450.00 + 300.00 + 250.00 = 1000.00 → 220 + 200 * 0.20 = 260.00),
    (20, 20, 20, 900 + 600 + 500 = 2000 → 220 + 200 * 0.20 = 260.00),
    # 输入验证失败（非整数）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 输入验证失败（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 销售额为0
    (0, 0, 0, 0.00),
    # 边界值测试（刚好等于1000）
    (22, 0, 0, 1000.00 * 0.10 = 100.00),
    # 边界值测试（刚好等于1800）
    (40, 0, 0, 1800.00 → 100 + 800 * 0.15 = 220.00),
    # 边界值测试（刚好大于1800）
    (41, 0, 0, 1845.00 → 220 + 45 * 0.20 = 229.00),
    # 非法输入（字符串）
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected