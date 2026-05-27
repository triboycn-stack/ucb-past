# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not (sales <= 1000)
# 重复次数: 3, 迭代: 4
# 生成时间: 2026-04-26 07:19:25

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("invalid", 1, 1, -1.0),
    (1, "invalid", 1, -1.0),
    (1, 1, "invalid", -1.0),
    (-1, 1, 1, -1.0),
    (1, -1, 1, -1.0),
    (1, 1, -1, -1.0),
    # 销售额 <= 1000
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (0, 3, 0, 9.00),
    (0, 0, 40, 100.00),
    # 销售额 <= 1800
    (0, 0, 41, 102.00),
    (1, 1, 10, 100.00 + (45+30+250 - 1000)*0.15),
    # 销售额 > 1800
    (0, 0, 73, 220 + (0 + 0 + 73*25 - 1800)*0.20),
    (2, 3, 50, 220 + (2*45 + 3*30 + 50*25 - 1800)*0.20),
    # 边界值测试
    (0, 0, 40, 100.00),
    (0, 0, 41, 102.00),
    (0, 0, 72, 220.00),
    (0, 0, 73, 220.00 + (73*25 - 1800)*0.20),
    # 非整数输入（字符串）
    ("123", "456", "789", -1.0),
    ("abc", "def", "ghi", -1.0),
    # 空值
    (None, None, None, -1.0),
    # 浮点数输入（应视为无效）
    (1.5, 2, 3, -1.0),
    (1, 2.5, 3, -1.0),
    (1, 2, 3.5, -1.0),
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected