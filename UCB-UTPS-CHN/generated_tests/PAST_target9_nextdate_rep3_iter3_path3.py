# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (day < 1 or day > max_day)
# 重复次数: 3, 迭代: 3
# 生成时间: 2026-04-26 07:06:24

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 31, "2023-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2023, 12, 31, "2024-01-01"),
    (2000, 12, 31, "2001-01-01"),
    (9999, 12, 31, "0000-01-01"),  # 年份边界测试

    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    (2023, 9, 31, "INVALID_DATE"),
    (2023, 11, 31, "INVALID_DATE"),
    (2023, 1, 0, "INVALID_DATE"),
    (2023, 1, 32, "INVALID_DATE"),

    # 非整数输入测试
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    (2023, 1.5, 1, "INVALID_DATE"),
    (2023, 1, 1.5, "INVALID_DATE"),
    (2023, None, 1, "INVALID_DATE"),
    (2023, 1, None, "INVALID_DATE"),
    (None, 1, 1, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected