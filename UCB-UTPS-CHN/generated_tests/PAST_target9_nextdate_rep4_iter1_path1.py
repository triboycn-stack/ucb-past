# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int))
# 重复次数: 4, 迭代: 1
# 生成时间: 2026-04-26 07:08:52

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 输入验证 - 非整数类型
    ("test", 1, 1, "INVALID_DATE"),
    (1, "test", 1, "INVALID_DATE"),
    (1, 1, "test", "INVALID_DATE"),
    # 年份边界检查
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 月份边界检查
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    # 日期有效性检查
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    # 正常情况 - 同月
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 30, "2020-12-31"),
    # 正常情况 - 月末
    (2020, 1, 31, "2020-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 4, 30, "2020-05-01"),
    # 正常情况 - 年末
    (2020, 12, 31, "2021-01-01"),
    # 闰年处理
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    # 年份超出范围
    (9999, 12, 31, "2000-01-01"),  # 由于下一年是10000，应返回DATE_OUT_OF_RANGE
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected