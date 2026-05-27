# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: year < 1 or year > 9999
# 重复次数: 3, 迭代: 2
# 生成时间: 2026-04-18 16:27:32

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 4, 15, "2021-04-16"),
    (2021, 12, 1, "2021-12-02"),
    (2021, 1, 1, "2021-01-02"),
    (2021, 12, 31, "2022-01-01"),
    
    # 无效年份测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    
    # 无效月份测试
    (2021, 0, 1, "INVALID_DATE"),
    (2021, 13, 1, "INVALID_DATE"),
    
    # 无效日期测试
    (2021, 2, 30, "INVALID_DATE"),
    (2021, 4, 31, "INVALID_DATE"),
    (2021, 1, 0, "INVALID_DATE"),
    (2021, 1, 32, "INVALID_DATE"),
    
    # 年末测试
    (2021, 12, 31, "2022-01-01"),
    
    # 年份边界测试
    (9999, 12, 31, "0001-01-01"),  # 注意：根据函数逻辑，这里会返回 "DATE_OUT_OF_RANGE"
    (9999, 12, 30, "10000-01-01"),  # 注意：根据函数逻辑，这里会返回 "DATE_OUT_OF_RANGE"
    
    # 非整数输入测试
    ("2021", 1, 1, "INVALID_DATE"),
    (2021, "1", 1, "INVALID_DATE"),
    (2021, 1, "1", "INVALID_DATE"),
    
    # 边界值测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected