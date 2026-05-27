# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (month < 1 or month > 12)
# 重复次数: 3, 迭代: 5
# 生成时间: 2026-04-26 07:06:51

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 1, 15, "2021-01-16"),
    (2021, 12, 1, "2021-12-02"),
    (2021, 11, 30, "2021-12-01"),
    (9999, 12, 31, "0001-01-01"),  # 年份边界测试

    # 无效输入测试
    ("test", 1, 1, "INVALID_DATE"),
    (1, "test", 1, "INVALID_DATE"),
    (1, 1, "test", "INVALID_DATE"),
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (1, 0, 1, "INVALID_DATE"),
    (1, 13, 1, "INVALID_DATE"),
    (1, 2, 30, "INVALID_DATE"),
    (1, 2, 0, "INVALID_DATE"),
    (1, 13, 31, "INVALID_DATE"),
    (1, 0, 31, "INVALID_DATE"),
    (1, 2, 31, "INVALID_DATE"),

    # 特殊情况测试
    (1, 1, 1, "0001-01-02"),
    (1, 12, 31, "0002-01-01"),
    (9999, 12, 31, "0001-01-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 12, 31, "2022-01-01"),
    (2021, 11, 30, "2021-12-01"),
    (2021, 11, 31, "INVALID_DATE"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 6, 30, "2021-07-01"),
    (2021, 9, 30, "2021-10-01"),
    (2021, 11, 30, "2021-12-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected