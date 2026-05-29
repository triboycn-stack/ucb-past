# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (day < 1 or day > max_day)
# 重复次数: 0, 迭代: 4
# 生成时间: 2026-04-18 16:13:06

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，非月末
    (2023, 4, 5, "2023-04-06"),
    # 有效日期，月末（非年末）
    (2023, 4, 30, "2023-05-01"),
    # 有效日期，年末
    (2023, 12, 31, "2024-01-01"),
    # 闰年二月最后一天
    (2020, 2, 29, "2020-03-01"),
    # 非闰年二月最后一天
    (2021, 2, 28, "2021-03-01"),
    # 月份边界测试（1月最后一天）
    (2023, 1, 31, "2023-02-01"),
    # 月份边界测试（12月最后一天）
    (2023, 12, 31, "2024-01-01"),
    # 年份边界测试（9999年12月31日）
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 输入验证：非整数
    ("2023", 4, 5, "INVALID_DATE"),
    ("2023", "4", 5, "INVALID_DATE"),
    ("2023", 4, "5", "INVALID_DATE"),
    # 输入验证：年份超出范围
    (0, 4, 5, "INVALID_DATE"),
    (10000, 4, 5, "INVALID_DATE"),
    # 输入验证：月份超出范围
    (2023, 0, 5, "INVALID_DATE"),
    (2023, 13, 5, "INVALID_DATE"),
    # 输入验证：日期超出范围（非二月）
    (2023, 4, 31, "INVALID_DATE"),
    # 输入验证：日期超出范围（二月）
    (2023, 2, 30, "INVALID_DATE"),
    # 输入验证：无效日期（负数）
    (2023, 4, -1, "INVALID_DATE"),
    # 输入验证：空值
    (None, 4, 5, "INVALID_DATE"),
    # 输入验证：字符串
    ("2023", "4", "5", "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected