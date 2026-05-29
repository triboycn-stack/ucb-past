# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (year < 1 or year > 9999)
# 重复次数: 1, 迭代: 6
# 生成时间: 2026-04-26 07:01:46

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2020, 4, 30, "2020-05-01"),
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 15, "2020-12-16"),
    (2020, 6, 1, "2020-06-02"),
    (9999, 12, 31, "0001-01-01"),  # 年份边界测试
    (1, 1, 1, "0001-01-02"),  # 年份边界测试

    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 9, 31, "INVALID_DATE"),
    (2020, 11, 31, "INVALID_DATE"),
    (2020, 2, 0, "INVALID_DATE"),
    (2020, 2, 31, "INVALID_DATE"),
    (2020, 1, 0, "INVALID_DATE"),
    (2020, 1, -1, "INVALID_DATE"),
    (2020, 1, 32, "INVALID_DATE"),

    # 类型错误测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    (2020, 1.5, 1, "INVALID_DATE"),
    (2020, 1, 1.5, "INVALID_DATE"),
    (None, 1, 1, "INVALID_DATE"),
    (2020, None, 1, "INVALID_DATE"),
    (2020, 1, None, "INVALID_DATE"),
    ([2020], 1, 1, "INVALID_DATE"),
    (2020, [1], 1, "INVALID_DATE"),
    (2020, 1, [1], "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected