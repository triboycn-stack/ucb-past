# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: day < max_day
# 重复次数: 0, 迭代: 10
# 生成时间: 2026-04-26 06:59:51

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，day < max_day
    (2023, 10, 5, "2023-10-06"),
    (2024, 2, 28, "2024-03-01"),  # 闰年2月28日
    (2023, 12, 30, "2023-12-31"),
    (2023, 11, 15, "2023-11-16"),
    
    # 有效日期，month < 12，day == max_day
    (2023, 10, 31, "2023-11-01"),
    (2023, 12, 31, "2024-01-01"),
    
    # 无效输入类型
    ("2023", 10, 5, "INVALID_DATE"),
    (2023, "10", 5, "INVALID_DATE"),
    (2023, 10, "5", "INVALID_DATE"),
    
    # 年份超出范围
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    
    # 月份超出范围
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    
    # 日期超出范围
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 12, 32, "INVALID_DATE"),
    
    # 边界情况：最小值
    (1, 1, 1, "0002-01-01"),
    (1, 1, 31, "0002-01-01"),
    
    # 边界情况：最大值
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected