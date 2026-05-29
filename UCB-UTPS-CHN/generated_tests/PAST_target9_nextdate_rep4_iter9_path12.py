# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 12
# 重复次数: 4, 迭代: 9
# 生成时间: 2026-04-18 16:30:50

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
    # 无效月份
    (2023, 13, 1, "INVALID_DATE"),
    # 无效年份
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 无效日期（超过当月最大天数）
    (2023, 2, 30, "INVALID_DATE"),
    # 无效日期（小于1）
    (2023, 1, 0, "INVALID_DATE"),
    # 无效类型
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    # 边界值：最小年份
    (1, 1, 1, "0002-01-01"),
    # 边界值：最大年份
    (9999, 12, 31, "0000-01-01"),
    # 月份边界：12
    (2023, 12, 31, "2024-01-01"),
    # 月份边界：1
    (2023, 1, 1, "2023-02-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected