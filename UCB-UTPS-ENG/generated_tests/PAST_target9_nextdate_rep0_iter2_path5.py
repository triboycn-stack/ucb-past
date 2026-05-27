# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (month < 1 or month > 12)
# 重复次数: 0, 迭代: 2
# 生成时间: 2026-04-18 16:12:38

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 12, 31, "2024-01-01"),
    (2024, 2, 28, "2024-03-01"),
    (2024, 2, 29, "2024-03-01"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 12, 15, "2023-12-16"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 12, 31, "2022-01-01"),
    (9999, 12, 31, "0001-01-01"),  # 年份边界测试

    # 无效输入测试
    ("invalid", 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    (0, 1, 1, "INVALID_DATE"),
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    (2023, 9, 31, "INVALID_DATE"),
    (2023, 11, 31, "INVALID_DATE"),
    (2023, 2, 0, "INVALID_DATE"),
    (2023, 2, 31, "INVALID_DATE"),
    (2023, 1, "invalid", "INVALID_DATE"),
    (2023, "invalid", 1, "INVALID_DATE"),
    (2023, 1, 32, "INVALID_DATE"),
    (2023, 1, -1, "INVALID_DATE"),
    (2023, 1, 0, "INVALID_DATE"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 1, "2023-01-02"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected