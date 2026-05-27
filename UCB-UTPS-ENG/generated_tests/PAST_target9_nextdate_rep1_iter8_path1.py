# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int))
# 重复次数: 1, 迭代: 8
# 生成时间: 2026-04-18 16:18:52

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
    # 日范围错误（非闰年二月）
    (2021, 2, 30, "INVALID_DATE"),
    # 日范围错误（闰年二月）
    (2020, 2, 30, "INVALID_DATE"),
    # 正常情况：非月末
    (2020, 1, 1, "2020-01-02"),
    # 正常情况：月末，非年末
    (2020, 1, 31, "2020-02-01"),
    # 正常情况：年末
    (2020, 12, 31, "2021-01-01"),
    # 边界情况：最小年份
    (1, 1, 1, "0001-01-02"),
    # 边界情况：最大年份
    (9999, 12, 31, "0001-01-01"),
    # 闰年二月最后一天
    (2020, 2, 29, "2020-03-01"),
    # 非闰年二月最后一天
    (2021, 2, 28, "2021-03-01"),
    # 月份天数验证
    (2020, 4, 30, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected