# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales < 0)
# 重复次数: 0, 迭代: 8
# 生成时间: 2026-04-26 07:13:39

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
    # 边界值测试
    (0, 0, 0, 0.00),
    (1, 1, 1, 10.00 + (45 + 30 + 25 - 1000) * 0.15),  # 销售额为 100
    (22, 22, 22, 100.00 + (22*45 + 22*30 + 22*25 - 1000) * 0.15),  # 销售额为 2200
    # 非法输入（类型错误）
    ("hello", 0, 0, -1.0),
    (0, "world", 0, -1.0),
    (0, 0, "test", -1.0),
    # 非法输入（负数）
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 非法输入（非整数）
    (1.5, 0, 0, -1.0),
    (0, 2.7, 0, -1.0),
    (0, 0, 3.3, -1.0),
    # 输入验证覆盖
    ("  hello\n    world", "  hello\n    world", "  hello\n    world", -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected