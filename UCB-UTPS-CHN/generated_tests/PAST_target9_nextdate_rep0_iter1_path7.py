# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: year < 1 or year > 9999
# 重复次数: 0, 迭代: 1
# 生成时间: 2026-04-18 16:12:24

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 12, 15, "2021-12-16"),
    (2021, 12, 31, "2022-01-01"),
    (2020, 1, 1, "2020-01-02"),
    
    # 年份边界测试
    (9999, 12, 31, "0001-01-01"),  # 注意：这里可能有逻辑问题，但按代码逻辑处理
    (1, 1, 1, "0001-01-02"),
    
    # 输入验证测试
    ("invalid", 1, 1, "INVALID_DATE"),
    (1, "invalid", 1, "INVALID_DATE"),
    (1, 1, "invalid", "INVALID_DATE"),
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (1, 0, 1, "INVALID_DATE"),
    (1, 13, 1, "INVALID_DATE"),
    (1, 2, 30, "INVALID_DATE"),
    (1, 2, 31, "INVALID_DATE"),
    (1, 4, 31, "INVALID_DATE"),
    (1, 6, 31, "INVALID_DATE"),
    (1, 9, 31, "INVALID_DATE"),
    (1, 11, 31, "INVALID_DATE"),
    
    # 闰年测试
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2024, 2, 29, "2024-03-01"),
    (2025, 2, 28, "2025-03-01"),
    
    # 边界值测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "0001-01-01"),
    (1, 1, 31, "INVALID_DATE"),
    (1, 12, 31, "0002-01-01"),
    (1, 12, 30, "0001-12-31"),
    (1, 12, 31, "0002-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected