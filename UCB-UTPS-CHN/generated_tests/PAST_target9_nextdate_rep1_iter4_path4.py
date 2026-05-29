# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 1 or month > 12
# 重复次数: 1, 迭代: 4
# 生成时间: 2026-04-26 07:01:26

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效输入
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 31, "2021-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 4, 30, "2020-05-01"),
    (2020, 6, 30, "2020-07-01"),
    (2020, 11, 30, "2020-12-01"),
    (2020, 1, 31, "2020-02-01"),
    (2020, 3, 31, "2020-04-01"),
    (2020, 5, 31, "2020-06-01"),
    (2020, 7, 31, "2020-08-01"),
    (2020, 8, 31, "2020-09-01"),
    (2020, 10, 31, "2020-11-01"),
    (2020, 12, 31, "2021-01-01"),
    # 无效输入（月份越界）
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    # 无效输入（年份越界）
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 无效输入（非整数）
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    # 无效输入（日期越界）
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 9, 31, "INVALID_DATE"),
    (2020, 11, 31, "INVALID_DATE"),
    # 年末处理
    (2020, 12, 31, "2021-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected