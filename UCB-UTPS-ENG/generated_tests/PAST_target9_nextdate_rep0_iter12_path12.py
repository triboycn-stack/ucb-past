# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 12
# 重复次数: 0, 迭代: 12
# 生成时间: 2026-04-26 07:00:09

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，非月末
    (2023, 10, 5, "2023-10-06"),
    # 有效日期，月末（非年末）
    (2023, 10, 31, "2023-11-01"),
    # 有效日期，年末
    (2023, 12, 31, "2024-01-01"),
    # 闰年2月28日
    (2020, 2, 28, "2020-03-01"),
    # 闰年2月29日
    (2020, 2, 29, "2020-03-01"),
    # 非闰年2月28日
    (2021, 2, 28, "2021-03-01"),
    # 非闰年2月29日（无效）
    (2021, 2, 29, "INVALID_DATE"),
    # 输入验证：非整数
    ("2023", 10, 5, "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    # 月份超出范围
    (2023, 13, 1, "INVALID_DATE"),
    # 日期超出范围
    (2023, 2, 30, "INVALID_DATE"),
    # 无效输入组合
    ("invalid", "invalid", "invalid", "INVALID_DATE"),
    # 边界值：最小年份
    (1, 1, 1, "0002-01-01"),
    # 边界值：最大年份
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 月份边界：12月
    (2023, 12, 1, "2023-12-02"),
    # 月份边界：1月
    (2023, 1, 31, "2023-02-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected