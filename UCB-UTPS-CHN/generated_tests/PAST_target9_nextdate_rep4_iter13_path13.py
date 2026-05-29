# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month == 2
# 重复次数: 4, 迭代: 13
# 生成时间: 2026-04-26 07:11:00

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 2, 28, "2020-03-01"),  # 闰年2月最后一天
    (2021, 2, 28, "2021-03-01"),  # 非闰年2月最后一天
    (2020, 2, 29, "2020-03-01"),  # 闰年2月29日
    (2021, 2, 28, "2021-03-01"),  # 非闰年2月28日
    (2020, 12, 31, "2021-01-01"),  # 年末
    (2020, 1, 1, "2020-01-02"),  # 月初
    (2020, 4, 30, "2020-05-01"),  # 月末
    (2020, 5, 15, "2020-05-16"),  # 中间日期

    # 无效输入测试
    ("invalid", 2, 28, "INVALID_DATE"),  # 年份非整数
    (2020, "invalid", 28, "INVALID_DATE"),  # 月份非整数
    (2020, 2, "invalid", "INVALID_DATE"),  # 日非整数
    (0, 2, 28, "INVALID_DATE"),  # 年份小于1
    (10000, 2, 28, "INVALID_DATE"),  # 年份大于9999
    (2020, 0, 28, "INVALID_DATE"),  # 月份小于1
    (2020, 13, 28, "INVALID_DATE"),  # 月份大于12
    (2020, 2, 30, "INVALID_DATE"),  # 2月30日无效
    (2020, 4, 31, "INVALID_DATE"),  # 4月31日无效
    (2020, 6, 31, "INVALID_DATE"),  # 6月31日无效
    (2020, 9, 31, "INVALID_DATE"),  # 9月31日无效
    (2020, 11, 31, "INVALID_DATE"),  # 11月31日无效

    # 边界条件测试
    (1, 1, 1, "0001-01-02"),  # 最小年份、月份、日期
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),  # 最大年份最后一天
    (2020, 2, 1, "2020-02-02"),  # 2月第一天
    (2020, 2, 29, "2020-03-01"),  # 闰年2月29日
    (2021, 2, 28, "2021-03-01"),  # 非闰年2月28日
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected