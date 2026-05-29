# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (day < 1 or day > max_day)
# 重复次数: 0, 迭代: 3
# 生成时间: 2026-04-26 06:58:40

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 12, 15, "2021-12-16"),
    (2021, 1, 1, "2021-01-02"),
    (2021, 12, 31, "2022-01-01"),
    
    # 无效日期测试（day超出范围）
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 4, 31, "INVALID_DATE"),
    (2021, 2, 0, "INVALID_DATE"),
    (2021, 13, 1, "INVALID_DATE"),
    (2021, 0, 1, "INVALID_DATE"),
    
    # 输入类型错误
    ("2021", 1, 1, "INVALID_DATE"),
    (2021, "1", 1, "INVALID_DATE"),
    (2021, 1, "1", "INVALID_DATE"),
    
    # 年份边界测试
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (9998, 12, 31, "1999-01-01"),
    
    # 闰年测试
    (2000, 2, 29, "2000-03-01"),
    (1900, 2, 29, "INVALID_DATE"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected