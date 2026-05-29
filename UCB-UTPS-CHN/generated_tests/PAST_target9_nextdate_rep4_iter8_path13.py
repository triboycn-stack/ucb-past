# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month == 2
# 重复次数: 4, 迭代: 8
# 生成时间: 2026-04-18 16:30:43

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效日期测试
    (2020, 2, 28, "2020-03-01"),  # 非闰年2月最后一天
    (2020, 2, 29, "2020-03-01"),  # 闰年2月最后一天
    (2021, 2, 28, "2021-03-01"),  # 非闰年2月最后一天
    (2024, 2, 29, "2024-03-01"),  # 闰年2月最后一天
    (2023, 2, 28, "2023-03-01"),  # 非闰年2月最后一天
    (2020, 12, 31, "2021-01-01"),  # 年末
    (2020, 1, 1, "2020-01-02"),  # 月初
    (2020, 12, 15, "2020-12-16"),  # 月中
    # 无效日期测试
    (2020, 2, 30, "INVALID_DATE"),  # 2月没有30天
    (2020, 13, 1, "INVALID_DATE"),  # 月份无效
    (0, 1, 1, "INVALID_DATE"),  # 年份无效
    (10000, 1, 1, "INVALID_DATE"),  # 年份无效
    (2020, 0, 1, "INVALID_DATE"),  # 月份无效
    (2020, 1, 0, "INVALID_DATE"),  # 日期无效
    (2020, 2, 30, "INVALID_DATE"),  # 2月没有30天
    # 边界条件测试
    (1, 1, 1, "0001-01-02"),  # 最小年份
    (9999, 12, 31, "0000-01-01"),  # 年份超出范围
    (9999, 12, 30, "9999-12-31"),  # 年份边界
    # 类型错误测试
    ("2020", 2, 28, "INVALID_DATE"),  # 年份不是整数
    (2020, "2", 28, "INVALID_DATE"),  # 月份不是整数
    (2020, 2, "28", "INVALID_DATE"),  # 日期不是整数
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected