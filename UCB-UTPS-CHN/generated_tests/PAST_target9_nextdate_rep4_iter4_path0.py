# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int)))
# 重复次数: 4, 迭代: 4
# 生成时间: 2026-04-18 16:30:05

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效输入，正常情况
    (2023, 1, 1, "2023-01-02"),
    (2023, 12, 31, "2024-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 12, 15, "2020-12-16"),
    (2024, 1, 31, "2024-02-01"),
    (2023, 4, 30, "2023-05-01"),
    (2023, 6, 30, "2023-07-01"),
    (2023, 9, 30, "2023-10-01"),
    (2023, 11, 30, "2023-12-01"),
    
    # 无效输入，类型错误
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    (2023, "a", 1, "INVALID_DATE"),
    (2023, 1, "a", "INVALID_DATE"),
    
    # 年份边界检查
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    (0, 1, 1, "INVALID_DATE"),
    
    # 月份边界检查
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    
    # 日子边界检查
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    (2023, 9, 31, "INVALID_DATE"),
    (2023, 11, 31, "INVALID_DATE"),
    
    # 闰年二月测试
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2022, 2, 28, "2022-03-01"),
    (2023, 2, 28, "2023-03-01"),
    (2024, 2, 29, "2024-03-01"),
    
    # 边界日期
    (1, 1, 1, "0002-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 12, 31, "0002-01-01"),
    (1, 1, 31, "INVALID_DATE"),
    (1, 2, 29, "INVALID_DATE"),
    (1, 2, 30, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected