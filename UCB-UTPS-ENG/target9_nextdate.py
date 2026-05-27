def next_date(year: int, month: int, day: int) -> str:
    """
    计算输入日期的下一天日期

    Args:
        year: 年份（1-9999）
        month: 月份（1-12）
        day: 日期（1-31）

    Returns:
        str: 下一天的日期，格式为 "YYYY-MM-DD"
             输入无效时返回 "INVALID_DATE"
    """
    # 输入验证
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        return "INVALID_DATE"

    if year < 1 or year > 9999:
        return "INVALID_DATE"

    if month < 1 or month > 12:
        return "INVALID_DATE"

    # 判断闰年
    def is_leap_year(y: int) -> bool:
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    # 每月天数
    days_in_month = [31, 28, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 确定二月天数
    if month == 2:
        max_day = 29 if is_leap_year(year) else 28
    else:
        max_day = days_in_month[month]

    if day < 1 or day > max_day:
        return "INVALID_DATE"

    # 计算下一天
    if day < max_day:
        # 同月下一天
        next_day = day + 1
        next_month = month
        next_year = year
    elif month < 12:
        # 月末，下个月第一天
        next_day = 1
        next_month = month + 1
        next_year = year
    else:
        # 年末，下一年的第一天
        next_day = 1
        next_month = 1
        next_year = year + 1

    # 年份边界检查
    if next_year > 9999:
        return "DATE_OUT_OF_RANGE"

    return f"{next_year:04d}-{next_month:02d}-{next_day:02d}"