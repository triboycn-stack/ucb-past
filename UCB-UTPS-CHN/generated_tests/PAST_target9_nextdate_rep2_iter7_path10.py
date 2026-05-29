# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: day < max_day
# 重复次数: 2, 迭代: 7
# 生成时间: 2026-04-18 16:25:51

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，day < max_day
    (2023, 10, 5, "2023-10-06"),
    (2024, 2, 28, "2024-02-29"),  # 闰年
    (2023, 12, 30, "2023-12-31"),
    (2023, 11, 30, "2023-12-01"),
    (2023, 1, 1, "2023-01-02"),
    # 无效日期，输入验证失败
    ("invalid", 1, 1, "INVALID_DATE"),
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    # 边界情况，day == max_day
    (2023, 12, 31, "2024-01-01"),
    (2024, 2, 29, "2024-03-01"),
    (2023, 11, 30, "2023-12-01"),
    # 年份边界检查
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (9998, 12, 31, "10000-01-01"),
    # 非法输入
    (2023, "invalid", 1, "INVALID_DATE"),
    (2023, 1, "invalid", "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected