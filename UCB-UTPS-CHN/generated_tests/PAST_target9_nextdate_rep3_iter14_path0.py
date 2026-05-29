# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int)))
# 重复次数: 3, 迭代: 14
# 生成时间: 2026-04-18 16:29:13

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效输入，非月末
    (2023, 10, 5, "2023-10-06"),
    # 有效输入，月末（非年末）
    (2023, 10, 31, "2023-11-01"),
    # 有效输入，年末
    (2023, 12, 31, "2024-01-01"),
    # 闰年二月最后一天
    (2020, 2, 29, "2020-03-01"),
    # 非闰年二月最后一天
    (2021, 2, 28, "2021-03-01"),
    # 月份边界测试（12月最后一天）
    (2023, 12, 31, "2024-01-01"),
    # 年份边界测试（9999年12月31日）
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 输入验证：非整数
    ("test", 1, 1, "INVALID_DATE"),
    (1, "test", 1, "INVALID_DATE"),
    (1, 1, "test", "INVALID_DATE"),
    # 输入验证：年份超出范围
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 输入验证：月份超出范围
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    # 输入验证：日期超出范围（非二月）
    (2023, 4, 31, "INVALID_DATE"),
    # 输入验证：日期超出范围（二月）
    (2023, 2, 30, "INVALID_DATE"),
    # 输入验证：无效的日期格式
    (2023, 2, 0, "INVALID_DATE"),
    # 输入验证：非法输入组合
    ("test", "test", "test", "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected