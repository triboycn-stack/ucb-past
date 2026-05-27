# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (day < max_day)
# 重复次数: 4, 迭代: 10
# 生成时间: 2026-04-18 16:30:59

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，非月末
    (2023, 10, 5, "2023-10-06"),
    # 有效日期，月末（非年末）
    (2023, 10, 31, "2023-11-01"),
    # 有效日期，年末
    (2023, 12, 31, "2024-01-01"),
    # 闰年二月最后一天
    (2020, 2, 29, "2020-03-01"),
    # 非闰年二月最后一天
    (2021, 2, 28, "2021-03-01"),
    # 输入验证失败（year不是整数）
    ("invalid", 1, 1, "INVALID_DATE"),
    # 输入验证失败（month不是整数）
    (2023, "invalid", 1, "INVALID_DATE"),
    # 输入验证失败（day不是整数）
    (2023, 1, "invalid", "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    # 月份无效
    (2023, 13, 1, "INVALID_DATE"),
    # 日期无效（超过当月最大天数）
    (2023, 2, 30, "INVALID_DATE"),
    # 日期无效（小于1）
    (2023, 1, 0, "INVALID_DATE"),
    # 日期无效（非闰年二月30日）
    (2023, 2, 30, "INVALID_DATE"),
    # 日期无效（闰年二月29日）
    (2024, 2, 29, "2024-03-01"),
    # 日期无效（闰年二月30日）
    (2024, 2, 30, "INVALID_DATE"),
    # 边界条件：最小年份
    (1, 1, 1, "0001-01-02"),
    # 边界条件：最大年份
    (9999, 12, 31, "0000-01-01"),
    # 边界条件：最大天数（非闰年二月）
    (2023, 2, 28, "2023-03-01"),
    # 边界条件：最大天数（闰年二月）
    (2024, 2, 29, "2024-03-01"),
    # 边界条件：最大月份
    (2023, 12, 31, "2024-01-01"),
    # 边界条件：最小月份
    (2023, 1, 1, "2023-01-02"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected