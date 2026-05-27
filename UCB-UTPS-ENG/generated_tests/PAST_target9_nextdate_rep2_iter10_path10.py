# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: day < max_day
# 重复次数: 2, 迭代: 10
# 生成时间: 2026-04-26 07:05:04

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，day < max_day
    (2023, 10, 5, "2023-10-06"),
    (2024, 2, 28, "2024-03-01"),  # 闰年二月
    (2023, 12, 30, "2023-12-31"),
    (2023, 4, 30, "2023-05-01"),  # 月末

    # 无效日期，输入验证失败
    ("invalid", 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (1, 13, 1, "INVALID_DATE"),
    (1, 1, 0, "INVALID_DATE"),
    (1, 1, 32, "INVALID_DATE"),

    # 闰年判断
    (2000, 2, 28, "2000-03-01"),
    (1900, 2, 28, "1900-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),

    # 年末处理
    (2023, 12, 31, "2024-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),

    # 边界情况
    (1, 1, 1, "0001-01-02"),
    (9999, 1, 1, "9999-01-02"),
    (1, 12, 31, "0002-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected