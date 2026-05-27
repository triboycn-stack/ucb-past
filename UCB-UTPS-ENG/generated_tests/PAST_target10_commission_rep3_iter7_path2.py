# 方法: PAST
# 目标文件: target10_commission.py
# 条件路径: locks < 0 or stocks < 0 or barrels < 0
# 重复次数: 3, 迭代: 7
# 生成时间: 2026-04-18 16:04:54

import pytest
from target10_commission import calculate_commission

@pytest.mark.parametrize("locks, stocks, barrels, expected", [
    # 输入验证测试
    ("  hello\n    world", 10, 5, -1.0),
    (10, "  hello\n    world", 5, -1.0),
    (10, 10, "  hello\n    world", -1.0),
    (10, 10, -5, -1.0),
    (-3, 10, 5, -1.0),
    (10, -2, 5, -1.0),
    (10, 10, -1, -1.0),
    (10, 10, 0, 220.0),  # 销售额刚好为1800
    (10, 10, 1, 220.0 + 25 * 0.20),  # 销售额超过1800
    (0, 0, 0, 0.0),  # 销售额为0
    (0, 0, 40, 1000.0),  # 销售额刚好为1000
    (0, 0, 41, 100 + (1025 - 1000) * 0.15),  # 销售额在1000到1800之间
    (10, 10, 10, 220.0),  # 销售额刚好为1800
    (10, 10, 11, 220.0 + 25 * 0.20),  # 销售额超过1800
    (5, 5, 5, 5*45 + 5*30 + 5*25),  # 销售额为450，计算佣金
    (0, 0, 0, 0.0),  # 全部为0
    (1, 1, 1, 45 + 30 + 25),  # 销售额为100，计算佣金
    (2, 2, 2, 2*45 + 2*30 + 2*25),  # 销售额为200，计算佣金
    (10, 0, 0, 10*45),  # 只卖锁
    (0, 10, 0, 10*30),  # 只卖股票
    (0, 0, 10, 10*25),  # 只卖枪管
])
def test_calculate_commission(locks, stocks, barrels, expected):
    result = calculate_commission(locks, stocks, barrels)
    assert result == expected