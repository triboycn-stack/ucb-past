# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: not isinstance(locks, int) or not isinstance(stocks, int) or (not isinstance(barrels, int))
# 重复次数: 1, 迭代: 1
# 生成时间: 2026-04-26 07:14:20

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (10, 10, 5, 220.0),  # 正常情况，销售额=10*45+10*30+5*25= 450+300+125=875 → 875*10% = 87.5 → round(87.5, 2) = 87.50
    (20, 10, 5, 220.0),  # 销售额=20*45+10*30+5*25=900+300+125=1325 → 100 + (1325-1000)*15% = 100 + 48.75 = 148.75 → round(148.75, 2) = 148.75
    (40, 10, 5, 220.0),  # 销售额=40*45+10*30+5*25=1800+300+125=2225 → 220 + (2225-1800)*20% = 220 + 85 = 305 → round(305, 2) = 305.00
    # 边界值测试
    (0, 0, 0, 0.00),
    (1, 0, 0, 4.50),
    (22, 0, 0, 99.00),  # 22*45=990 → 990*10% = 99.00
    (23, 0, 0, 100 + (1035-1000)*15% = 100 + 5.25 = 105.25)
    (40, 0, 0, 220 + (1800-1800)*20% = 220.00)
    (41, 0, 0, 220 + (1845-1800)*20% = 220 + 9 = 229.00)
    # 负数输入
    (-1, 0, 0, -1.0),
    (0, -1, 0, -1.0),
    (0, 0, -1, -1.0),
    # 非整数类型
    (10.5, 10, 5, -1.0),
    (10, 10.5, 5, -1.0),
    (10, 10, 5.5, -1.0),
    # 大数值测试（防止溢出）
    (1000000, 0, 0, 220 + (45000000 - 1800)*0.20 = 220 + 8999640 = 9000000.00)
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected