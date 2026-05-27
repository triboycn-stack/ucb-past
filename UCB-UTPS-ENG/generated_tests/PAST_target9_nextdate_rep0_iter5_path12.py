# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 12
# 重复次数: 0, 迭代: 5
# 生成时间: 2026-04-18 16:13:18

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，非月末
    (2023, 4, 5, "2023-04-06"),
    # 有效日期，月末，非年末
    (2023, 4, 30, "2023-05-01"),
    # 有效日期，年末
    (2023, 12, 31, "2024-01-01"),
    # 无效输入：年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    # 无效输入：月份超出范围
    (2023, 13, 1, "INVALID_DATE"),
    # 无效输入：日期超出范围（非闰年二月）
    (2023, 2, 30, "INVALID_DATE"),
    # 无效输入：日期超出范围（闰年二月）
    (2024, 2, 30, "INVALID_DATE"),
    # 无效输入：非整数参数
    ("2023", 4, 5, "INVALID_DATE"),
    # 无效输入：空值
    (None, 4, 5, "INVALID_DATE"),
    # 边界条件：最小年份
    (1, 1, 1, "0002-01-01"),
    # 边界条件：最大年份
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 闰年测试：2月28日
    (2020, 2, 28, "2020-03-01"),
    # 闰年测试：2月29日
    (2020, 2, 29, "2020-03-01"),
    # 非闰年测试：2月28日
    (2021, 2, 28, "2021-03-01"),
    # 非闰年测试：2月29日
    (2021, 2, 29, "INVALID_DATE"),
    # 月份为12，日期为31
    (2023, 12, 31, "2024-01-01"),
    # 月份为11，日期为30
    (2023, 11, 30, "2023-12-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected