# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 12
# 重复次数: 3, 迭代: 12
# 生成时间: 2026-04-26 07:08:08

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
    # 输入验证失败（非整数）
    ("2023", 10, 5, "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    # 月份无效
    (2023, 13, 1, "INVALID_DATE"),
    # 日期无效（超过当月最大天数）
    (2023, 2, 30, "INVALID_DATE"),
    # 日期无效（小于1）
    (2023, 1, 0, "INVALID_DATE"),
    # 月份边界测试（month < 12）
    (2023, 11, 30, "2023-12-01"),
    # 月份边界测试（month == 12）
    (2023, 12, 31, "2024-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected