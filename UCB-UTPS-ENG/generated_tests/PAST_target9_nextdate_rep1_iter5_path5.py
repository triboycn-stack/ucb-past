# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (month < 1 or month > 12)
# 重复次数: 1, 迭代: 5
# 生成时间: 2026-04-26 07:01:36

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 4, 30, "2019-05-01"),
    (2020, 6, 15, "2020-06-16"),
    
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
    
    # 边界值测试
    (1, 1, 1, "0002-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (2020, 1, 31, "2020-02-01"),
    (2020, 3, 31, "2020-04-01"),
    (2020, 5, 31, "2020-06-01"),
    (2020, 7, 31, "2020-08-01"),
    (2020, 8, 31, "2020-09-01"),
    (2020, 10, 31, "2020-11-01"),
    (2020, 12, 31, "2021-01-01"),
    
    # 非整数输入测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    (2020, 1.5, 1, "INVALID_DATE"),
    (2020, 1, 1.5, "INVALID_DATE"),
    (None, 1, 1, "INVALID_DATE"),
    (2020, None, 1, "INVALID_DATE"),
    (2020, 1, None, "INVALID_DATE"),
    
    # 条件分支覆盖测试
    (2020, 1, 31, "2020-02-01"),  # 同月下一天
    (2020, 2, 29, "2020-03-01"),  # 月末，下个月第一天
    (2020, 12, 31, "2021-01-01"),  # 年末，下一年第一天
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected