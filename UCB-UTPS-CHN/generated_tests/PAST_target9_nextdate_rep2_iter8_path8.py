# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: next_year > 9999
# 重复次数: 2, 迭代: 8
# 生成时间: 2026-04-26 07:04:43

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
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 9, 31, "INVALID_DATE"),
    (2020, 11, 31, "INVALID_DATE"),
    
    # 输入类型错误测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (9999, 1, 1, "2000-01-02"),
    (9998, 12, 31, "10000-01-01"),
    
    # 条件分支覆盖测试
    (2020, 1, 31, "2020-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2020, 12, 31, "2021-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected