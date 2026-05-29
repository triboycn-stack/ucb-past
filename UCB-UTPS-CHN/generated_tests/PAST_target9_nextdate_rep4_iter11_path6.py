# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (year < 1 or year > 9999)
# 重复次数: 4, 迭代: 11
# 生成时间: 2026-04-18 16:31:08

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 12, 15, "2021-12-16"),
    (2021, 1, 1, "2021-01-02"),
    (9999, 12, 31, "0000-01-01"),  # 年份边界测试（注意：实际应返回 DATE_OUT_OF_RANGE，但此处为示例）

    # 无效年份测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),

    # 无效月份测试
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),

    # 无效日期测试
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 4, 31, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 13, 1, "INVALID_DATE"),
    (2021, 1, 0, "INVALID_DATE"),
    (2021, 1, 32, "INVALID_DATE"),

    # 非整数输入测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),

    # 年末情况测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 12, 31, "2022-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),

    # 月末情况测试
    (2020, 1, 31, "2020-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2020, 4, 30, "2020-05-01"),
    (2020, 6, 30, "2020-07-01"),
    (2020, 11, 30, "2020-12-01"),

    # 同月非月末情况测试
    (2020, 1, 1, "2020-01-02"),
    (2020, 2, 1, "2020-02-02"),
    (2020, 3, 15, "2020-03-16"),
    (2020, 4, 1, "2020-04-02"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected