# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 12
# 重复次数: 2, 迭代: 12
# 生成时间: 2026-04-26 07:05:23

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
    # 输入验证：类型错误
    ("2023", 10, 5, "INVALID_DATE"),
    ("2023", "10", 5, "INVALID_DATE"),
    (2023, 10, "5", "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    (0, 1, 1, "DATE_OUT_OF_RANGE"),
    # 月份无效
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    # 日期无效（非二月）
    (2023, 4, 31, "INVALID_DATE"),
    # 日期无效（二月）
    (2023, 2, 30, "INVALID_DATE"),
    # 边界条件：最小年份
    (1, 1, 1, "0002-01-01"),
    # 边界条件：最大年份
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 边界条件：最大月份
    (2023, 12, 1, "2023-12-02"),
    # 边界条件：最大日
    (2023, 12, 31, "2024-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected