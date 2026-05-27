# 方法: PAST
# 目标文件: target9_nextdate.py
# 条件路径: month < 1 or month > 12
# 重复次数: 0, 迭代: 4
# 生成时间: 2026-04-26 06:58:48

import pytest
from target9_nextdate import next_date

@pytest.mark.parametrize("year, month, day, expected", [
    # 有效输入，非月末
    (2023, 10, 5, "2023-10-06"),
    # 有效输入，月末（非年末）
    (2023, 10, 31, "2023-11-01"),
    # 有效输入，年末
    (2023, 12, 31, "2024-01-01"),
    # 无效月份（小于1）
    (2023, 0, 1, "INVALID_DATE"),
    # 无效月份（大于12）
    (2023, 13, 1, "INVALID_DATE"),
    # 无效年份（小于1）
    (0, 1, 1, "INVALID_DATE"),
    # 无效年份（大于9999）
    (10000, 1, 1, "INVALID_DATE"),
    # 无效天数（小于1）
    (2023, 1, 0, "INVALID_DATE"),
    # 无效天数（大于当月最大天数）
    (2023, 2, 30, "INVALID_DATE"),
    # 闰年2月30日（非法）
    (2020, 2, 30, "INVALID_DATE"),
    # 非闰年2月29日（非法）
    (2021, 2, 29, "INVALID_DATE"),
    # 年份超出范围
    (9999, 12, 31, "2000-01-01"),
    # 参数类型错误（year不是int）
    ("2023", 1, 1, "INVALID_DATE"),
    # 参数类型错误（month不是int）
    (2023, "1", 1, "INVALID_DATE"),
    # 参数类型错误（day不是int）
    (2023, 1, "1", "INVALID_DATE"),
])
def test_next_date(year, month, day, expected):
    result = next_date(year, month, day)
    assert result == expected