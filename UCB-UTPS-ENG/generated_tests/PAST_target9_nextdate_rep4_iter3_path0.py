# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int)))
# 重复次数: 4, 迭代: 3
# 生成时间: 2026-04-18 16:29:55

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 4, 15, "2021-04-16"),
    (2021, 12, 1, "2021-12-02"),
    (2021, 1, 31, "2021-02-01"),
    (2020, 12, 15, "2020-12-16"),
    
    # 输入验证测试
    ("invalid", 1, 1, "INVALID_DATE"),
    (1, "invalid", 1, "INVALID_DATE"),
    (1, 1, "invalid", "INVALID_DATE"),
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (1, 0, 1, "INVALID_DATE"),
    (1, 13, 1, "INVALID_DATE"),
    (1, 1, 0, "INVALID_DATE"),
    (1, 1, 32, "INVALID_DATE"),
    
    # 边界条件测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 1, 31, "0001-02-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 12, 31, "2021-01-01"),
    
    # 异常情况测试
    (None, 1, 1, "INVALID_DATE"),
    (1, None, 1, "INVALID_DATE"),
    (1, 1, None, "INVALID_DATE"),
    (1.5, 1, 1, "INVALID_DATE"),
    (1, 1.5, 1, "INVALID_DATE"),
    (1, 1, 1.5, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected