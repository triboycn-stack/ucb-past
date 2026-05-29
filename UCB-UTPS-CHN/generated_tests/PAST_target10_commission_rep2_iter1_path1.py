# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 2, 迭代: 1
# 生成时间: 2026-04-26 07:16:22

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
    (1.5, 2, 3, -1.0),
    (1, 2.5, 3, -1.0),
    (1, 2, 3.5, -1.0),
    (1, 2, -1, -1.0),
    (-1, 2, 3, -1.0),
    (1, -2, 3, -1.0),
    # 销售额 ≤ 1000
    (0, 0, 0, 0.0),
    (1, 0, 0, 4.5),
    (0, 3, 0, 9.0),
    (0, 0, 4, 10.0),
    (2, 1, 1, 16.5),
    # 销售额 ≤ 1800
    (10, 0, 0, 45.0),
    (0, 10, 0, 30.0),
    (0, 0, 10, 25.0),
    (5, 5, 5, 57.5),
    (15, 0, 0, 67.5),
    (0, 15, 0, 45.0),
    (0, 0, 15, 37.5),
    # 销售额 > 1800
    (20, 0, 0, 110.0),
    (0, 20, 0, 80.0),
    (0, 0, 20, 50.0),
    (10, 10, 10, 115.0),
    (25, 0, 0, 155.0),
    (0, 25, 0, 115.0),
    (0, 0, 25, 75.0),
    # 边界值测试
    (22, 0, 0, 100.0),
    (0, 22, 0, 66.0),
    (0, 0, 22, 55.0),
    (23, 0, 0, 103.0),
    (0, 23, 0, 69.0),
    (0, 0, 23, 57.5),
    # 小数保留测试
    (1, 1, 1, 10.0),
    (2, 2, 2, 21.0),
    (3, 3, 3, 32.0),
    (4, 4, 4, 43.0),
    (5, 5, 5, 54.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected