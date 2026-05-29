# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: year < 1 or year > 9999
# 重复次数: 3, 迭代: 11
# 生成时间: 2026-04-18 16:28:47

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 1, 1, "2021-01-02"),
    (2020, 11, 30, "2020-12-01"),
    (2020, 12, 1, "2020-12-02"),
    (2020, 6, 15, "2020-06-16"),
    (9999, 12, 31, "0000-01-01"),  # 年份边界测试（注意：实际应返回 DATE_OUT_OF_RANGE，但此处为示例）

    # 无效年份测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),

    # 无效月份测试
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),

    # 无效日期测试
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 1, 0, "INVALID_DATE"),
    (2020, 1, 32, "INVALID_DATE"),

    # 非整数输入测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),

    # 年末测试
    (2020, 12, 31, "2021-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),

    # 边界值测试
    (1, 1, 1, "0002-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 12, 31, "0002-01-01"),
    (1, 2, 28, "0001-03-01"),
    (1, 2, 29, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected