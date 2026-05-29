# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: next_year > 9999
# 重复次数: 0, 迭代: 9
# 生成时间: 2026-04-18 16:14:16

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 1, 1, "2021-01-02"),
    (2021, 12, 15, "2021-12-16"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 6, 15, "2021-06-16"),
    (2021, 11, 30, "2021-12-01"),
    (2021, 12, 31, "2022-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2021, 6, 31, "INVALID_DATE"),
    (2021, 11, 31, "INVALID_DATE"),
    (2021, 12, 32, "INVALID_DATE"),
    
    # 参数类型错误测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    (2020, 1.5, 1, "INVALID_DATE"),
    (2020, 1, 1.5, "INVALID_DATE"),
    (None, 1, 1, "INVALID_DATE"),
    (2020, None, 1, "INVALID_DATE"),
    (2020, 1, None, "INVALID_DATE"),
    
    # 边界条件测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 12, 31, "0002-01-01"),
    (1, 2, 28, "0001-03-01"),
    (1, 2, 29, "INVALID_DATE"),
    (1, 1, 31, "0001-02-01"),
    (1, 3, 31, "0001-04-01"),
    (1, 4, 30, "0001-05-01"),
    (1, 5, 31, "0001-06-01"),
    (1, 6, 30, "0001-07-01"),
    (1, 7, 31, "0001-08-01"),
    (1, 8, 31, "0001-09-01"),
    (1, 9, 30, "0001-10-01"),
    (1, 10, 31, "0001-11-01"),
    (1, 11, 30, "0001-12-01"),
    (1, 12, 31, "0002-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected