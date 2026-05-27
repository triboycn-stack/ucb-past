# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: day < max_day
# 重复次数: 2, 迭代: 11
# 生成时间: 2026-04-18 16:26:28

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，day < max_day
    (2023, 10, 5, "2023-10-06"),
    (2024, 2, 28, "2024-02-29"),  # 闰年
    (2023, 12, 30, "2023-12-31"),
    (2020, 1, 15, "2020-01-16"),
    # 有效日期，月末，下个月第一天
    (2023, 10, 31, "2023-11-01"),
    (2024, 2, 29, "2024-03-01"),  # 闰年
    (2023, 12, 31, "2024-01-01"),
    # 无效日期（day > max_day）
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    # 无效输入类型
    ("2023", 10, 5, "INVALID_DATE"),
    (2023, "10", 5, "INVALID_DATE"),
    (2023, 10, "5", "INVALID_DATE"),
    # 年份边界检查
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 非法月份
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    # 非法年份
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 非法日
    (2023, 1, 0, "INVALID_DATE"),
    (2023, 1, 32, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected