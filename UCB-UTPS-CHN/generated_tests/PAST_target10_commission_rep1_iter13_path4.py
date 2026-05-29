# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales <= 1000)
# 重复次数: 1, 迭代: 13
# 生成时间: 2026-04-18 15:58:20

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
    # 销售额 ≤ 1000
    (0, 0, 0, 0.0),
    (1, 0, 0, 4.5),
    (0, 3, 0, 9.0),
    (0, 0, 4, 10.0),
    (2, 1, 1, 16.0),
    # 销售额 ≤ 1800
    (10, 0, 0, 45.0),
    (0, 10, 0, 30.0),
    (0, 0, 10, 25.0),
    (5, 5, 5, 57.5),
    # 销售额 > 1800
    (20, 0, 0, 90.0),
    (0, 20, 0, 60.0),
    (0, 0, 20, 50.0),
    (10, 10, 10, 145.0),
    # 边界值测试
    (0, 0, 40, 100.0),
    (0, 0, 41, 100.0 + 25 * 0.15),
    (0, 0, 72, 220.0),
    (0, 0, 73, 220.0 + 25 * 0.20),
    # 复杂组合
    (10, 10, 10, 145.0),
    (20, 20, 20, 240.0),
    (5, 5, 50, 137.5),
    (100, 0, 0, 450.0),
    # 非整数输入（应返回-1.0）
    (1.5, 0, 0, -1.0),
    (0, 2.5, 0, -1.0),
    (0, 0, 3.5, -1.0),
    # 非数字字符串输入（应返回-1.0）
    ("abc", 0, 0, -1.0),
    (0, "def", 0, -1.0),
    (0, 0, "ghi", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected