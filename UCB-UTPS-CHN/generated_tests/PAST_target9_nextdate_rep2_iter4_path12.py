# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 12
# 重复次数: 2, 迭代: 4
# 生成时间: 2026-04-18 16:25:23

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 6, 15, "2021-06-16"),
    
    # 无效输入测试
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
    
    # 边界条件测试
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (1, 12, 31, "0002-01-01"),
    (2020, 12, 31, "2021-01-01"),
    (2021, 12, 31, "2022-01-01"),
    
    # 条件分支测试（month < 12）
    (2020, 11, 30, "2020-12-01"),
    (2020, 11, 1, "2020-11-02"),
    (2020, 12, 1, "2020-12-02"),
    (2020, 12, 31, "2021-01-01"),
    
    # 异常处理测试
    (None, 1, 1, "INVALID_DATE"),
    (1, None, 1, "INVALID_DATE"),
    (1, 1, None, "INVALID_DATE"),
    (1.0, 1, 1, "INVALID_DATE"),
    (1, 1.0, 1, "INVALID_DATE"),
    (1, 1, 1.0, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected