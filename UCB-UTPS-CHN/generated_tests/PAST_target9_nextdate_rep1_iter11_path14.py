# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (month < 12)
# 重复次数: 1, 迭代: 11
# 生成时间: 2026-04-18 16:21:08

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 31, "2023-02-01"),
    (2024, 2, 28, "2024-03-01"),
    (2024, 2, 29, "2024-03-01"),
    (2023, 12, 31, "2024-01-01"),
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
    
    # 边界条件测试
    (1, 1, 1, "0002-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (2023, 1, 1, "2023-01-02"),
    (2023, 12, 31, "2024-01-01"),
    
    # 类型错误测试
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    (2023, 1.5, 1, "INVALID_DATE"),
    (2023, 1, 1.5, "INVALID_DATE"),
    
    # 条件分支测试（not (month < 12)）
    (2023, 12, 1, "2024-01-01"),
    (2023, 11, 30, "2023-12-01"),
    (2023, 12, 31, "2024-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected