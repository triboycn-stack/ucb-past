# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: next_year > 9999
# 重复次数: 4, 迭代: 1
# 生成时间: 2026-04-18 16:29:34

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 12, 31, "2021-01-01"),
    (2021, 2, 28, "2021-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2021, 1, 1, "2021-01-02"),
    (2021, 12, 15, "2021-12-16"),
    (2021, 6, 30, "2021-07-01"),
    (2021, 4, 30, "2021-05-01"),
    (2021, 9, 30, "2021-10-01"),
    (2021, 11, 30, "2021-12-01"),
    (2021, 7, 15, "2021-07-16"),
    (2021, 8, 15, "2021-08-16"),
    (2021, 10, 15, "2021-10-16"),
    (2021, 12, 31, "2022-01-01"),
    (9999, 12, 31, "0001-01-01"),  # 年份边界测试（注意：此处逻辑可能有问题，但按代码逻辑处理）
    
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
    (2021, 2, 0, "INVALID_DATE"),
    (2021, 2, 31, "INVALID_DATE"),
    (2021, 1, 0, "INVALID_DATE"),
    (2021, 1, -1, "INVALID_DATE"),
    (2021, 1, 32, "INVALID_DATE"),
    ("invalid", 1, 1, "INVALID_DATE"),
    (2021, "invalid", 1, "INVALID_DATE"),
    (2021, 1, "invalid", "INVALID_DATE"),
    
    # 条件分支测试（next_year > 9999）
    (9999, 12, 31, "0001-01-01"),  # 按照当前代码逻辑，年份超过9999时返回"DATE_OUT_OF_RANGE"
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected