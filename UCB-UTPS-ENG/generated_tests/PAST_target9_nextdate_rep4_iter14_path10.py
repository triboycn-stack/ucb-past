# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: day < max_day
# 重复次数: 4, 迭代: 14
# 生成时间: 2026-04-18 16:31:49

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，day < max_day
    (2023, 10, 5, "2023-10-06"),
    (2024, 2, 28, "2024-03-01"),  # 闰年二月
    (2023, 12, 30, "2023-12-31"),
    (2023, 11, 15, "2023-11-16"),
    # 有效日期，月末，下个月第一天
    (2023, 10, 31, "2023-11-01"),
    (2023, 12, 31, "2024-01-01"),
    # 无效日期（月份错误）
    (2023, 13, 1, "INVALID_DATE"),
    # 无效日期（天数超过当月最大天数）
    (2023, 2, 30, "INVALID_DATE"),
    # 无效日期（非整数输入）
    (2023, "12", 1, "INVALID_DATE"),
    (2023, 12, "1", "INVALID_DATE"),
    # 年份边界检查
    (9999, 12, 31, "0000-01-01"),
    (9999, 1, 1, "10000-01-01"),
    # 非法输入（年份超出范围）
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    (0, 1, 1, "DATE_OUT_OF_RANGE"),
    # 边界情况：最小值
    (1, 1, 1, "0001-01-02"),
    # 边界情况：最大值
    (9999, 12, 31, "0000-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected