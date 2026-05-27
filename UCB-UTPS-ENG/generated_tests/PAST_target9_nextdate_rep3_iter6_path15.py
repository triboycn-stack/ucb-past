# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (month == 2)
# 重复次数: 3, 迭代: 6
# 生成时间: 2026-04-18 16:28:05

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2023, 1, 1, "2023-01-02"),
    (2023, 1, 31, "2023-02-01"),
    (2020, 2, 28, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2024, 2, 29, "2024-03-01"),
    (2023, 12, 31, "2024-01-01"),
    
    # 无效输入测试
    ("invalid", 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (1, 13, 1, "INVALID_DATE"),
    (1, 1, 0, "INVALID_DATE"),
    (1, 1, 32, "INVALID_DATE"),
    
    # 边界条件测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 12, 31, "0002-01-01"),
    
    # 闰年测试
    (2000, 2, 29, "2000-03-01"),
    (1900, 2, 28, "1900-03-01"),
    (2012, 2, 29, "2012-03-01"),
    (2013, 2, 28, "2013-03-01"),
    
    # 条件分支覆盖测试（month != 2）
    (2023, 3, 15, "2023-03-16"),
    (2023, 4, 30, "2023-05-01"),
    (2023, 6, 30, "2023-07-01"),
    (2023, 9, 30, "2023-10-01"),
    (2023, 11, 30, "2023-12-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected