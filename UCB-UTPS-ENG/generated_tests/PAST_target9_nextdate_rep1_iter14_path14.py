# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (month < 12)
# 重复次数: 1, 迭代: 14
# 生成时间: 2026-04-26 07:03:02

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 1, 1, "2023-01-02"),
    (2023, 12, 31, "2024-01-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2023, 4, 30, "2023-05-01"),
    (2023, 6, 15, "2023-06-16"),
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    (2023, 2, 30, "INVALID_DATE"),
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    (2023, 9, 31, "INVALID_DATE"),
    (2023, 11, 31, "INVALID_DATE"),
    
    # 类型错误测试
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (9998, 12, 31, "2000-01-01"),
    
    # 条件分支测试（not (month < 12)）
    (2023, 12, 1, "2024-01-01"),
    (2023, 11, 30, "2023-12-01"),
    (2023, 12, 31, "2024-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected