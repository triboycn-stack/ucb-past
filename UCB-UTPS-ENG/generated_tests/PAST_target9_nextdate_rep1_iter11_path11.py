# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (day < max_day)
# 重复次数: 1, 迭代: 11
# 生成时间: 2026-04-26 07:02:34

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
    # 输入验证：非整数
    ("test", 1, 1, "INVALID_DATE"),
    ("123", 1, 1, "INVALID_DATE"),
    (1, "test", 1, "INVALID_DATE"),
    (1, 1, "test", "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    (0, 1, 1, "INVALID_DATE"),
    # 月份超出范围
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    # 日期超出范围
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 1, 0, "INVALID_DATE"),
    # 边界条件：最小年份
    (1, 1, 1, "0001-01-02"),
    # 边界条件：最大年份
    (9999, 12, 31, "0000-01-01"),
    # 特殊情况：下一年第一天
    (9999, 12, 31, "0000-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected