# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 1 or month > 12
# 重复次数: 2, 迭代: 4
# 生成时间: 2026-04-26 07:04:02

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效输入
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 31, "2021-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2019, 12, 31, "2020-01-01"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 6, 30, "2021-07-01"),
    (2021, 1, 31, "2021-02-01"),
    # 无效输入（月份范围）
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    # 无效输入（年份范围）
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 无效输入（天数范围）
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    # 非整数输入
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    # 年末情况
    (2020, 12, 31, "2021-01-01"),
    # 闰年二月
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    # 边界值测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 空值
    (None, 1, 1, "INVALID_DATE"),
    (1, None, 1, "INVALID_DATE"),
    (1, 1, None, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected