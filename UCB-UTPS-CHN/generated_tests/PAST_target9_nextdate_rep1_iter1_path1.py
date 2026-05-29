# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int))
# 重复次数: 1, 迭代: 1
# 生成时间: 2026-04-26 07:00:54

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 无效输入类型
    ("test", 1, 1, "INVALID_DATE"),
    (1, "test", 1, "INVALID_DATE"),
    (1, 1, "test", "INVALID_DATE"),
    # 年份范围错误
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 月份范围错误
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    # 日范围错误（非闰年2月）
    (2021, 2, 30, "INVALID_DATE"),
    # 日范围错误（闰年2月）
    (2020, 2, 30, "INVALID_DATE"),
    # 正常日期，非月末
    (2020, 1, 1, "2020-01-02"),
    # 正常日期，月末（非年末）
    (2020, 1, 31, "2020-02-01"),
    # 正常日期，年末
    (2020, 12, 31, "2021-01-01"),
    # 闰年2月28日
    (2020, 2, 28, "2020-03-01"),
    # 非闰年2月28日
    (2021, 2, 28, "2021-03-01"),
    # 闰年2月29日（非法）
    (2020, 2, 29, "INVALID_DATE"),
    # 年份边界检查
    (9999, 12, 31, "0001-01-01"),
    # 无效日期（日超出当月最大天数）
    (2020, 4, 31, "INVALID_DATE"),
    # 有效日期，跨月
    (2020, 4, 30, "2020-05-01"),
    # 有效日期，跨年
    (2020, 12, 31, "2021-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected