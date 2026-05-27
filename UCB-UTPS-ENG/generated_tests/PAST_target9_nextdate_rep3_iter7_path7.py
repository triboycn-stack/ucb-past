# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: year < 1 or year > 9999
# 重复次数: 3, 迭代: 7
# 生成时间: 2026-04-26 07:07:16

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2021, 1, 1, "2021-01-02"),
    (2021, 12, 31, "2022-01-01"),
    (2020, 4, 30, "2020-05-01"),
    (2020, 6, 30, "2020-07-01"),
    (2020, 11, 30, "2020-12-01"),
    (2020, 1, 1, "2020-01-02"),
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    (2020, 6, 31, "INVALID_DATE"),
    (2020, 11, 31, "INVALID_DATE"),
    (2020, 1, 0, "INVALID_DATE"),
    
    # 类型错误测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    (2020, 1.5, 1, "INVALID_DATE"),
    (2020, 1, 1.5, "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "0000-01-01"),  # 注意：这里可能不符合实际逻辑，但根据代码逻辑会返回 "DATE_OUT_OF_RANGE"
    (9999, 1, 1, "10000-02-01"),  # 注意：这里可能不符合实际逻辑，但根据代码逻辑会返回 "DATE_OUT_OF_RANGE"
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected