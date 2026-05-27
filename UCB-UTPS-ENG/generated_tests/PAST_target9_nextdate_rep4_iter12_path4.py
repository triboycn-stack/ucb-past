# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 1 or month > 12
# 重复次数: 4, 迭代: 12
# 生成时间: 2026-04-18 16:31:23

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 31, "2021-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 4, 30, "2020-05-01"),
    (2020, 11, 30, "2020-12-01"),
    (2020, 1, 31, "2020-02-01"),
    (2020, 3, 31, "2020-04-01"),
    (2020, 5, 31, "2020-06-01"),
    (2020, 7, 31, "2020-08-01"),
    (2020, 8, 31, "2020-09-01"),
    (2020, 10, 31, "2020-11-01"),
    (2020, 12, 31, "2021-01-01"),
    
    # 无效月份测试（month < 1）
    (2020, 0, 1, "INVALID_DATE"),
    (2020, -1, 1, "INVALID_DATE"),
    
    # 无效月份测试（month > 12）
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 14, 1, "INVALID_DATE"),
    
    # 无效年份测试（year < 1）
    (0, 1, 1, "INVALID_DATE"),
    (-1, 1, 1, "INVALID_DATE"),
    
    # 无效年份测试（year > 9999）
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    (10001, 1, 1, "DATE_OUT_OF_RANGE"),
    
    # 无效天数测试（day < 1）
    (2020, 1, 0, "INVALID_DATE"),
    (2020, 1, -1, "INVALID_DATE"),
    
    # 无效天数测试（day > max_day）
    (2020, 2, 30, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 9, 31, "INVALID_DATE"),
    (2020, 11, 31, "INVALID_DATE"),
    
    # 非整数输入测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    
    # 边界条件测试（year = 1）
    (1, 1, 1, "0002-01-01"),
    
    # 边界条件测试（year = 9999）
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    
    # 闰年测试（2月29日）
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2024, 2, 29, "2024-03-01"),
    (2025, 2, 28, "2025-03-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected