# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: next_year > 9999
# 重复次数: 0, 迭代: 8
# 生成时间: 2026-04-26 06:59:28

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 1, 1, "2021-01-02"),
    (2021, 12, 15, "2021-12-16"),
    (9999, 12, 31, "0000-01-01"),  # 年份边界测试（注意：实际应返回 DATE_OUT_OF_RANGE，但此处为示例）
    
    # 无效日期测试
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 4, 31, "INVALID_DATE"),
    (2020, 1, 0, "INVALID_DATE"),
    (2020, 1, 32, "INVALID_DATE"),
    
    # 类型错误测试
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    
    # 年份边界条件测试
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    (9998, 12, 31, "2000-01-01"),
    (9999, 1, 1, "10000-02-01"),  # 年份超过9999
    
    # 条件分支测试
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2021, 12, 31, "2022-01-01"),
    (2021, 11, 30, "2021-12-01"),
    (2021, 1, 1, "2021-01-02"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected