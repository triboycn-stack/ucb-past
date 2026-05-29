# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: not (day < 1 or day > max_day)
# 重复次数: 2, 迭代: 0
# 生成时间: 2026-04-18 16:24:36

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期，非月末
    (2023, 10, 5, "2023-10-06"),
    # 有效日期，月末（非年末）
    (2023, 10, 31, "2023-11-01"),
    # 有效日期，年末
    (2023, 12, 31, "2024-01-01"),
    # 闰年二月最后一天
    (2020, 2, 29, "2020-03-01"),
    # 非闰年二月最后一天
    (2021, 2, 28, "2021-03-01"),
    # 月份天数验证（例如4月31日无效）
    (2023, 4, 31, "INVALID_DATE"),
    # 年份边界测试（9999年12月31日）
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 输入类型错误（字符串）
    ("2023", 10, 5, "INVALID_DATE"),
    # 年份超出范围
    (10000, 1, 1, "INVALID_DATE"),
    # 月份超出范围
    (2023, 13, 1, "INVALID_DATE"),
    # 日期超出范围
    (2023, 10, 32, "INVALID_DATE"),
    # 无效输入（非整数）
    (2023, "10", 5, "INVALID_DATE"),
    # 空值
    (None, 10, 5, "INVALID_DATE"),
    # 边界值：最小年份
    (1, 1, 1, "0001-01-02"),
    # 边界值：最大年份
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 边界值：最小月份
    (2023, 1, 1, "2023-02-01"),
    # 边界值：最大月份
    (2023, 12, 31, "2024-01-01"),
    # 边界值：最小日期
    (2023, 1, 1, "2023-02-01"),
    # 边界值：最大日期（非闰年二月）
    (2023, 2, 28, "2023-03-01"),
    # 边界值：最大日期（闰年二月）
    (2020, 2, 29, "2020-03-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected