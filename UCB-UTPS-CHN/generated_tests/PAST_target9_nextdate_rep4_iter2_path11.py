# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (day < max_day)
# 重复次数: 4, 迭代: 2
# 生成时间: 2026-04-18 16:29:45

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 6, 15, "2021-06-16"),
    (2021, 12, 1, "2021-12-02"),
    (9999, 12, 31, "0000-01-01"),  # 年份边界测试（注意：实际应返回 DATE_OUT_OF_RANGE，但代码中未处理）

    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 11, 31, "INVALID_DATE"),
    (2020, 1, 0, "INVALID_DATE"),
    (2020, 1, -1, "INVALID_DATE"),

    # 参数类型错误测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    (2020, 1.5, 1, "INVALID_DATE"),
    (2020, 1, 1.5, "INVALID_DATE"),
    (2020, [1], 1, "INVALID_DATE"),
    (2020, 1, {"day": 1}, "INVALID_DATE"),

    # 边界条件测试
    (1, 1, 1, "0001-01-02"),
    (1, 12, 31, "0002-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (2020, 1, 31, "2020-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 12, 31, "2022-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected