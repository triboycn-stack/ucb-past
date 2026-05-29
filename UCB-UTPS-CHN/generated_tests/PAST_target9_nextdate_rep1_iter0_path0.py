# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int)))
# 重复次数: 1, 迭代: 0
# 生成时间: 2026-04-26 07:00:46

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 31, "2023-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2023, 12, 31, "2024-01-01"),
    (2024, 12, 31, "2025-01-01"),
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
    
    # 边界值测试
    (1, 1, 1, "0002-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 12, 31, "0002-01-01"),
    (1, 2, 28, "0001-03-01"),
    (1, 2, 29, "INVALID_DATE"),
    
    # 闰年测试
    (2000, 2, 29, "2000-03-01"),
    (1900, 2, 28, "1900-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected