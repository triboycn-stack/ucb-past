# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (year < 1 or year > 9999)
# 重复次数: 2, 迭代: 6
# 生成时间: 2026-04-26 07:04:22

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 1, 1, "2021-01-02"),
    (2021, 12, 15, "2021-12-16"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 6, 30, "2021-07-01"),
    (2021, 11, 30, "2021-12-01"),
    (2021, 12, 31, "2022-01-01"),
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2021, 0, 1, "INVALID_DATE"),
    (2021, 13, 1, "INVALID_DATE"),
    (2021, 2, 30, "INVALID_DATE"),
    (2021, 4, 31, "INVALID_DATE"),
    (2021, 6, 31, "INVALID_DATE"),
    (2021, 9, 31, "INVALID_DATE"),
    (2021, 11, 31, "INVALID_DATE"),
    
    # 类型错误测试
    ("2021", 1, 1, "INVALID_DATE"),
    (2021, "1", 1, "INVALID_DATE"),
    (2021, 1, "1", "INVALID_DATE"),
    
    # 边界值测试
    (1, 1, 1, "0002-01-01"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 12, 31, "0002-01-01"),
    (1, 2, 28, "0001-03-01"),
    (1, 2, 29, "INVALID_DATE"),
    (9999, 1, 1, "10000-01-02"),
    
    # 特殊情况测试
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 12, 31, "2022-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected