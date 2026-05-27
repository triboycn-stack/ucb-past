# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales < 0)
# 重复次数: 1, 迭代: 8
# 生成时间: 2026-04-26 07:15:28

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 有效输入，销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),
    # 有效输入，销售额在 1000-1800 之间
    (23, 0, 0, 100.00 + (1035 - 1000) * 0.15),
    (10, 10, 10, 100.00 + (10*45 + 10*30 + 10*25 - 1000) * 0.15),
    # 有效输入，销售额 > 1800
    (40, 0, 0, 220 + (1800 - 1800) * 0.20),
    (41, 0, 0, 220 + (1845 - 1800) * 0.20),
    # 输入验证：非整数
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 输入验证：负数
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 边界情况：销售额为0
    (0, 0, 0, 0.00),
    # 销售额刚好等于1000
    (22, 0, 0, 99.00),
    # 销售额刚好等于1800
    (40, 0, 0, 220.00),
    # 销售额略高于1800
    (41, 0, 0, 220 + (1845 - 1800) * 0.20),
    # 非法输入（字符串）
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected