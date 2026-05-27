# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not isinstance(year, int) or not isinstance(month, int) or (not isinstance(day, int))
# 重复次数: 3, 迭代: 1
# 生成时间: 2026-04-26 07:06:05

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 输入验证 - 非整数类型
    ("test", 1, 1, "INVALID_DATE"),
    (1, "test", 1, "INVALID_DATE"),
    (1, 1, "test", "INVALID_DATE"),
    # 年份边界检查
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 月份边界检查
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    # 日期有效性检查
    (2020, 2, 30, "INVALID_DATE"),
    (2019, 2, 29, "INVALID_DATE"),
    # 正常日期 - 非月末
    (2020, 5, 15, "2020-05-16"),
    # 正常日期 - 月末（非年末）
    (2020, 5, 31, "2020-06-01"),
    # 正常日期 - 年末
    (2020, 12, 31, "2021-01-01"),
    # 闰年二月
    (2020, 2, 29, "2020-03-01"),
    # 非闰年二月
    (2021, 2, 28, "2021-03-01"),
    # 年份超出范围
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected