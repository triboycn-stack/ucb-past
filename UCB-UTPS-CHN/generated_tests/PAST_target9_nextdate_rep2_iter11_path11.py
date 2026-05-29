# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (day < max_day)
# 重复次数: 2, 迭代: 11
# 生成时间: 2026-04-26 07:05:13

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，非月末
    (2023, 10, 5, "2023-10-06"),
    # 有效日期，月末（非年末）
    (2023, 10, 31, "2023-11-01"),
    # 有效日期，年末
    (2023, 12, 31, "2024-01-01"),
    # 无效年份
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 无效月份
    (2023, 0, 1, "INVALID_DATE"),
    (2023, 13, 1, "INVALID_DATE"),
    # 无效日期（非闰年二月）
    (2023, 2, 29, "INVALID_DATE"),
    # 无效日期（闰年二月）
    (2024, 2, 29, "2024-03-01"),
    # 无效输入类型
    ("2023", 1, 1, "INVALID_DATE"),
    (2023, "1", 1, "INVALID_DATE"),
    (2023, 1, "1", "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "INVALID_DATE"),
    (9999, 12, 31, "2000-01-01"),
    # 边界情况：最小年份
    (1, 1, 1, "0002-01-01"),
    # 边界情况：最大年份
    (9999, 12, 31, "0001-01-01"),
    # 闰年二月
    (2020, 2, 29, "2020-03-01"),
    # 非闰年二月
    (2021, 2, 28, "2021-03-01"),
    # 月份天数验证
    (2023, 4, 31, "INVALID_DATE"),
    (2023, 6, 31, "INVALID_DATE"),
    (2023, 9, 31, "INVALID_DATE"),
    (2023, 11, 31, "INVALID_DATE"),
    # 月份天数验证（非二月）
    (2023, 2, 28, "2023-03-01"),
    (2023, 2, 29, "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected