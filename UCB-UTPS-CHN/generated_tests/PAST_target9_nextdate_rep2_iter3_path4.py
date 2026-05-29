# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 1 or month > 12
# 重复次数: 2, 迭代: 3
# 生成时间: 2026-04-18 16:25:12

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效输入
    (2020, 12, 31, "2021-01-01"),
    (2020, 2, 28, "2020-03-01"),
    (2020, 2, 29, "2020-03-01"),
    (2019, 2, 28, "2019-03-01"),
    (2020, 4, 30, "2020-05-01"),
    (2020, 1, 1, "2020-01-02"),
    (2020, 12, 15, "2020-12-16"),
    # 无效月份
    (2020, 0, 1, "INVALID_DATE"),
    (2020, 13, 1, "INVALID_DATE"),
    # 无效年份
    (0, 1, 1, "INVALID_DATE"),
    (10000, 1, 1, "INVALID_DATE"),
    # 无效日期
    (2020, 2, 30, "INVALID_DATE"),
    (2021, 2, 29, "INVALID_DATE"),
    (2020, 4, 31, "INVALID_DATE"),
    # 年末情况
    (2020, 12, 31, "2021-01-01"),
    # 边界情况
    (1, 1, 1, "0001-01-02"),
    (9999, 12, 31, "DATE_OUT_OF_RANGE"),
    # 非整数输入
    ("2020", 1, 1, "INVALID_DATE"),
    (2020, "1", 1, "INVALID_DATE"),
    (2020, 1, "1", "INVALID_DATE"),
    # 无效参数类型
    (2020, 1.5, 1, "INVALID_DATE"),
    (2020, 1, 1.5, "INVALID_DATE"),
    # 闰年测试
    (2020, 2, 29, "2020-03-01"),
    (2021, 2, 28, "2021-03-01"),
    (2000, 2, 29, "2000-03-01"),
    (1900, 2, 28, "1900-03-01"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected