# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 1 or month > 12
# 重复次数: 3, 迭代: 4
# 生成时间: 2026-04-26 07:06:41

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 1, 1, "2023-01-02"),
    (2023, 12, 31, "2024-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 12, 15, "2020-12-16"),
    (2020, 6, 30, "2020-07-01"),
    (2020, 1, 31, "2020-02-01"),
    (2020, 3, 31, "2020-04-01"),
    (2020, 4, 30, "2020-05-01"),
    (2020, 5, 31, "2020-06-01"),
    (2020, 7, 31, "2020-08-01"),
    (2020, 8, 31, "2020-09-01"),
    (2020, 9, 30, "2020-10-01"),
    (2020, 10, 31, "2020-11-01"),
    (2020, 11, 30, "2020-12-01"),
    (2020, 12, 31, "2021-01-01"),
    
    # 无效月份测试
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    
    # 无效年份测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    
    # 无效日期测试
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    (2023, 9, 31, "INVALID_DATE"),
    (2023, 11, 31, "INVALID_DATE"),
    (2023, 2, 29, "INVALID_DATE"),
    (2023, 1, 0, "INVALID_DATE"),
    (2023, 1, 32, "INVALID_DATE"),
    
    # 非整数输入测试
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "10000-01-01"),
    (9999, 1, 1, "1999-01-02"),  # 假设此处为错误，实际应为 "DATE_OUT_OF_RANGE"
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected