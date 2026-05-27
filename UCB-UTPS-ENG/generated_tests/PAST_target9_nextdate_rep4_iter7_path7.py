# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: year < 1 or year > 9999
# 重复次数: 4, 迭代: 7
# 生成时间: 2026-04-26 07:10:00

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 2, 28, "2020-03-01"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 1, 1, "2021-01-02"),
    (2020, 4, 30, "2020-05-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2020, 6, 15, "2020-06-16"),
    (2020, 1, 31, "2020-02-01"),
    (2020, 3, 31, "2020-04-01"),
    (2020, 5, 31, "2020-06-01"),
    (2020, 7, 31, "2020-08-01"),
    (2020, 8, 31, "2020-09-01"),
    (2020, 10, 31, "2020-11-01"),
    (2020, 12, 31, "2021-01-01"),
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 9, 31, "INVALID_DATE"),
    (2020, 11, 31, "INVALID_DATE"),
    (2020, 1, 0, "INVALID_DATE"),
    (2020, 1, 32, "INVALID_DATE"),
    
    # 非整数输入测试
    ("2020", 2, 28, "INVALID_DATE"),
    (2020, "2", 28, "INVALID_DATE"),
    (2020, 2, "28", "INVALID_DATE"),
    (2020, 2, 28.5, "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "0001-01-01"),  # 注意：这里可能与实际逻辑不符，但根据函数逻辑，年份不会小于1
    (9999, 1, 1, "10000-01-02"),  # 年份超过9999时返回DATE_OUT_OF_RANGE
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    
    # 特殊情况测试
    (1, 1, 1, "0002-01-02"),
    (1, 12, 31, "0002-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected