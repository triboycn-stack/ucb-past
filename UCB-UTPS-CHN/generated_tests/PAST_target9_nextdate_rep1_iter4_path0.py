# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int)))
# 重复次数: 1, 迭代: 4
# 生成时间: 2026-04-18 16:16:49

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效输入，非月末
    (2023, 10, 5, "2023-10-06"),
    # 有效输入，月末（非年末）
    (2023, 10, 31, "2023-11-01"),
    # 有效输入，年末
    (2023, 12, 31, "2024-01-01"),
    # 闰年二月
    (2020, 2, 29, "2020-03-01"),
    # 非闰年二月
    (2021, 2, 28, "2021-03-01"),
    # 无效输入：年份超出范围
    (10000, 1, 1, "DATE_OUT_OF_RANGE"),
    # 无效输入：月份超出范围
    (2023, 13, 1, "INVALID_DATE"),
    # 无效输入：日期超出当月最大值
    (2023, 2, 30, "INVALID_DATE"),
    # 无效输入：非整数参数
    ("2023", 1, 1, "INVALID_DATE"),
    ("2023", "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    # 无效输入：年份小于1
    (0, 1, 1, "INVALID_DATE"),
    # 无效输入：月份为0
    (2023, 0, 1, "INVALID_DATE"),
    # 无效输入：日期为0
    (2023, 1, 0, "INVALID_DATE"),
    # 边界条件：最小年份
    (1, 1, 1, "0002-01-01"),
    # 边界条件：最大年份
    (9999, 12, 31, "0001-01-01"),
    # 边界条件：最大日期
    (2023, 12, 31, "2024-01-01"),
    # 边界条件：最小日期
    (1, 1, 1, "0002-01-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected