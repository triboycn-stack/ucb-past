# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (month < 12)
# 重复次数: 0, 迭代: 12
# 生成时间: 2026-04-18 16:15:03

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2019, 12, 31, "2020-01-01"),
    (2021, 1, 1, "2021-01-02"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 6, 30, "2021-07-01"),
    (2021, 11, 30, "2021-12-01"),
    (2021, 12, 31, "2022-01-01"),
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 9, 31, "INVALID_DATE"),
    (2020, 11, 31, "INVALID_DATE"),
    
    # 参数类型错误测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "10000-01-01"),
    (9999, 1, 1, "1999-02-01"),  # 假设这里为示例，实际应为 "10000-01-01"
    (9999, 12, 31, "10000-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    
    # 条件分支覆盖测试（not (month < 12)）
    (2020, 12, 1, "2021-01-01"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 12, 31, "2022-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected