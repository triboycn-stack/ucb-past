# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: day < 1 or day > max_day
# 重复次数: 1, 迭代: 2
# 生成时间: 2026-04-26 07:01:05

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
    
    # 无效日期测试（day < 1）
    (2023, 1, 0, "INVALID_DATE"),
    (2023, 2, 0, "INVALID_DATE"),
    
    # 无效日期测试（day > max_day）
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    
    # 月份边界测试
    (2023, 12, 31, "2024-01-01"),
    (2023, 12, 1, "2023-12-02"),
    
    # 年份边界测试
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (9999, 12, 1, "2000-01-01"),
    
    # 输入类型错误测试
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    
    # 月份无效测试
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    
    # 年份无效测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected