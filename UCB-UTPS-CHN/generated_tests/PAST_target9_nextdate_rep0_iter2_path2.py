# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: day < 1 or day > max_day
# 重复次数: 0, 迭代: 2
# 生成时间: 2026-04-26 06:58:33

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 1, 1, "2023-01-02"),
    (2023, 12, 31, "2024-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 12, 31, "2021-01-01"),
    (2020, 6, 15, "2020-06-16"),
    (2020, 1, 31, "2020-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 11, 30, "2020-12-01"),
    
    # 无效日期测试（day < 1）
    (2023, 1, 0, "INVALID_DATE"),
    (2023, 2, 0, "INVALID_DATE"),
    
    # 无效日期测试（day > max_day）
    (2023, 1, 32, "INVALID_DATE"),
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    (2023, 9, 31, "INVALID_DATE"),
    (2023, 11, 31, "INVALID_DATE"),
    
    # 输入类型错误
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    
    # 年份范围错误
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    
    # 月份范围错误
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    
    # 年末处理
    (2023, 12, 31, "2024-01-01"),
    (2099, 12, 31, "2100-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    
    # 闰年处理
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2000, 2, 29, "2000-03-01"),
    (1900, 2, 28, "1900-03-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected