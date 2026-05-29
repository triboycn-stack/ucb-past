# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: year < 1 or year > 9999
# 重复次数: 0, 迭代: 7
# 生成时间: 2026-04-26 06:59:19

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
    (1, 1, 1, "0002-01-01"),
    (9999, 12, 31, "0001-01-01"),
    
    # 无效年份测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    
    # 无效月份测试
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    
    # 无效日期测试
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 4, 31, "INVALID_DATE"),
    (2020, 12, 0, "INVALID_DATE"),
    (2020, 12, 32, "INVALID_DATE"),
    
    # 非整数输入测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "0001-01-01"),
    (9999, 1, 1, "10000-01-02"),
    (9999, 12, 31, "0001-01-01"),
    
    # 特殊情况测试
    (1, 1, 1, "0002-01-01"),
    (1, 12, 31, "0002-01-01"),
    (9999, 1, 1, "10000-01-02"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected