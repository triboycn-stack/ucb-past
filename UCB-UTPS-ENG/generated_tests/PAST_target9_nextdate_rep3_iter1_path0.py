# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int)))
# 重复次数: 3, 迭代: 1
# 生成时间: 2026-04-18 16:27:22

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
    
    # 无效输入类型测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 1, 1, "0002-01-01"),
    
    # 月份边界测试
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    
    # 日子边界测试
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2021, 6, 31, "INVALID_DATE"),
    
    # 闰年测试
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2000, 2, 29, "2000-03-01"),
    (1900, 2, 28, "1900-03-01"),
    
    # 月末测试
    (2020, 1, 31, "2020-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2020, 4, 30, "2020-05-01"),
    
    # 年末测试
    (2020, 12, 31, "2021-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    
    # 非法输入测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 1, 0, "INVALID_DATE"),
    (2020, 1, 32, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected