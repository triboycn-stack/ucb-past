# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int)))
# 重复次数: 2, 迭代: 8
# 生成时间: 2026-04-18 16:26:01

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 12, 31, "2024-01-01"),
    (2024, 2, 28, "2024-03-01"),
    (2024, 2, 29, "2024-03-01"),
    (2023, 4, 30, "2023-05-01"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 12, 15, "2023-12-16"),
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    (2023, 9, 31, "INVALID_DATE"),
    (2023, 11, 31, "INVALID_DATE"),
    
    # 边界值测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "0000-01-01"),
    (2023, 12, 31, "2024-01-01"),
    (2024, 12, 31, "2025-01-01"),
    
    # 类型错误测试
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    (2023, 1, 1.5, "INVALID_DATE"),
    
    # 闰年测试
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2024, 2, 29, "2024-03-01"),
    (2025, 2, 28, "2025-03-01"),
    
    # 年份边界测试
    (9999, 12, 31, "0000-01-01"),
    (9999, 12, 30, "9999-12-31"),
    (9999, 12, 31, "0000-01-01"),
    (9998, 12, 31, "9999-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected