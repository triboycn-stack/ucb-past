# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int))
# 重复次数: 3, 迭代: 13
# 生成时间: 2026-04-18 16:29:06

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 输入验证错误
    ("test", 1, 1, "INVALID_DATE"),
    (1, "test", 1, "INVALID_DATE"),
    (1, 1, "test", "INVALID_DATE"),
    (1.5, 1, 1, "INVALID_DATE"),
    (1, 1.5, 1, "INVALID_DATE"),
    (1, 1, 1.5, "INVALID_DATE"),
    # 年份边界
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 月份边界
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    # 日期边界（非闰年二月）
    (2021, 2, 29, "INVALID_DATE"),
    # 日期边界（闰年二月）
    (2020, 2, 30, "INVALID_DATE"),
    # 正常日期
    (2020, 1, 1, "2020-01-02"),
    (2020, 1, 31, "2020-02-01"),
    (2020, 2, 28, "2020-03-01"),
    (2020, 12, 31, "2021-01-01"),
    # 边界情况
    (1, 1, 1, "0002-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 月末处理
    (2020, 4, 30, "2020-05-01"),
    (2020, 6, 30, "2020-07-01"),
    # 闰年处理
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected