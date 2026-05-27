# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int)))
# 重复次数: 4, 迭代: 0
# 生成时间: 2026-04-26 07:08:44

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 1, 15, "2021-01-16"),
    (2021, 12, 15, "2021-12-16"),
    (2021, 11, 30, "2021-12-01"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 6, 30, "2021-07-01"),
    (2021, 9, 30, "2021-10-01"),
    (2021, 11, 30, "2021-12-01"),
    (2021, 1, 31, "2021-02-01"),
    (2021, 3, 31, "2021-04-01"),
    (2021, 5, 31, "2021-06-01"),
    (2021, 7, 31, "2021-08-01"),
    (2021, 8, 31, "2021-09-01"),
    (2021, 10, 31, "2021-11-01"),
    (2021, 12, 31, "2022-01-01"),
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2021, 0, 1, "INVALID_DATE"),
    (2021, 13, 1, "INVALID_DATE"),
    (2021, 2, 30, "INVALID_DATE"),
    (2021, 4, 31, "INVALID_DATE"),
    (2021, 6, 31, "INVALID_DATE"),
    (2021, 9, 31, "INVALID_DATE"),
    (2021, 11, 31, "INVALID_DATE"),
    (2021, 2, 0, "INVALID_DATE"),
    (2021, 1, 32, "INVALID_DATE"),
    (2021, 12, 32, "INVALID_DATE"),
    
    # 非整数输入测试
    ("2021", 1, 1, "INVALID_DATE"),
    (2021, "1", 1, "INVALID_DATE"),
    (2021, 1, "1", "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (9998, 12, 31, "9999-01-01"),
    
    # 特殊情况测试
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 12, 31, "2022-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected