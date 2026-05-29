# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: day < max_day
# 重复次数: 4, 迭代: 10
# 生成时间: 2026-04-26 07:10:31

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，day < max_day
    (2023, 10, 5, "2023-10-06"),
    (2024, 2, 28, "2024-03-01"),  # 闰年，day < max_day
    (2023, 12, 30, "2023-12-31"),
    (2023, 1, 1, "2023-01-02"),
    # 有效日期，月末，下个月第一天
    (2023, 10, 31, "2023-11-01"),
    (2023, 2, 28, "2023-03-01"),
    (2024, 2, 29, "2024-03-01"),
    (2023, 12, 31, "2024-01-01"),
    # 无效输入
    ("invalid", 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    (1, 0, 1, "INVALID_DATE"),
    (1, 13, 1, "INVALID_DATE"),
    (1, 1, 0, "INVALID_DATE"),
    (1, 1, 32, "INVALID_DATE"),
    (1, 2, 30, "INVALID_DATE"),
    # 边界情况
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "0001-01-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected