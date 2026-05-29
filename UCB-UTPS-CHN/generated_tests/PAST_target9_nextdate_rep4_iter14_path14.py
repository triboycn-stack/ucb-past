# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (month < 12)
# 重复次数: 4, 迭代: 14
# 生成时间: 2026-04-26 07:11:08

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
    
    # 无效输入测试
    ("invalid", 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    (1, 0, 1, "INVALID_DATE"),
    (1, 13, 1, "INVALID_DATE"),
    (1, 1, 0, "INVALID_DATE"),
    (1, 1, 32, "INVALID_DATE"),
    (1, 2, 30, "INVALID_DATE"),
    (1, 4, 31, "INVALID_DATE"),
    
    # 边界条件测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 12, 31, "0002-01-01"),
    (2020, 12, 31, "2021-01-01"),
    
    # 条件分支测试（not (month < 12)）
    (2023, 12, 1, "2023-12-02"),
    (2023, 12, 31, "2024-01-01"),
    (2023, 11, 30, "2023-12-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected