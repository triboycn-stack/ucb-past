# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 12
# 重复次数: 1, 迭代: 12
# 生成时间: 2026-04-26 07:02:43

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，非月末，非年末
    (2023, 4, 5, "2023-04-06"),
    # 有效日期，月末，非年末
    (2023, 4, 30, "2023-05-01"),
    # 有效日期，年末
    (2023, 12, 31, "2024-01-01"),
    # 闰年2月最后一天
    (2020, 2, 29, "2020-03-01"),
    # 非闰年2月最后一天
    (2021, 2, 28, "2021-03-01"),
    # 月份边界测试（month < 12）
    (2023, 11, 30, "2023-12-01"),
    # 月份边界测试（month == 12）
    (2023, 12, 31, "2024-01-01"),
    # 输入验证：非整数
    ("2023", 4, 5, "INVALID_DATE"),
    ("2023", "4", 5, "INVALID_DATE"),
    ("2023", 4, "5", "INVALID_DATE"),
    # 输入验证：年份越界
    (0, 4, 5, "INVALID_DATE"),
    (10000, 4, 5, "INVALID_DATE"),
    # 输入验证：月份越界
    (2023, 0, 5, "INVALID_DATE"),
    (2023, 13, 5, "INVALID_DATE"),
    # 输入验证：日期越界（非二月）
    (2023, 4, 31, "INVALID_DATE"),
    # 输入验证：日期越界（二月）
    (2023, 2, 30, "INVALID_DATE"),
    # 年份越界（下一年超过9999）
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 无效输入组合
    ("invalid", "invalid", "invalid", "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected