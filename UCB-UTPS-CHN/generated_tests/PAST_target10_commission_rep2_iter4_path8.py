# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales < 0)
# 重复次数: 2, 迭代: 4
# 生成时间: 2026-04-18 15:59:36

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    # 有效输入，销售额在 1000-1800 之间
    (23, 0, 0, 100.00 + (1035 - 1000) * 0.15),
    (25, 0, 0, 100.00 + (1125 - 1000) * 0.15),
    # 有效输入，销售额 > 1800
    (40, 0, 0, 220 + (1800 - 1800) * 0.20),
    (41, 0, 0, 220 + (1845 - 1800) * 0.20),
    # 混合商品销售
    (10, 10, 10, 220 + (10*45 + 10*30 + 10*25 - 1800) * 0.20),
    # 边界值测试
    (0, 0, 0, 0.00),
    (1, 1, 1, 10.00),
    # 非法输入（非整数）
    ("  hello\n    world", 0, 0, -1.0),
    (0, "  hello\n    world", 0, -1.0),
    (0, 0, "  hello\n    world", -1.0),
    # 非法输入（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 销售额为负数（理论上不可能，但测试边界检查）
    (0, 0, 1000000, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected