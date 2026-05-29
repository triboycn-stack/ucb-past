# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month == 2
# 重复次数: 2, 迭代: 13
# 生成时间: 2026-04-26 07:05:32

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 2, 28, "2020-03-01"),  # 非闰年2月最后一天
    (2020, 2, 29, "2020-03-01"),  # 闰年2月最后一天
    (2021, 2, 28, "2021-03-01"),  # 非闰年2月最后一天
    (2024, 2, 29, "2024-03-01"),  # 闰年2月最后一天
    (2023, 2, 28, "2023-03-01"),  # 非闰年2月最后一天

    # 无效日期测试
    (2020, 2, 30, "INVALID_DATE"),  # 2月30日无效
    (2021, 2, 30, "INVALID_DATE"),  # 2月30日无效
    (2020, 13, 1, "INVALID_DATE"),  # 月份无效
    (2020, 0, 1, "INVALID_DATE"),   # 月份无效
    (2020, 2, 0, "INVALID_DATE"),   # 日无效
    (2020, 2, -1, "INVALID_DATE"),  # 日无效

    # 边界条件测试
    (1, 1, 1, "0001-01-02"),        # 最小年份、最小月份、最小日
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),  # 年末，下一年超出范围

    # 类型错误测试
    ("2020", 2, 28, "INVALID_DATE"),  # 年份不是整数
    (2020, "2", 28, "INVALID_DATE"),  # 月份不是整数
    (2020, 2, "28", "INVALID_DATE"),  # 日不是整数
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected