# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 0, 迭代: 6
# 生成时间: 2026-05-23 09:19:36

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 基本情况：正常字符串，以双引号结束
    ("\"hello world\"", 1, True, "hello world", 13),
    # 转义字符：转义双引号
    ("\"hello\\\"world\"", 1, True, "hello\"world", 14),
    # 转义字符：转义反斜杠
    ("\"hello\\\\world\"", 1, True, "hello\\world", 14),
    # 多个转义字符
    ("\"hello\\\\\\\"world\"", 1, True, "hello\\\"world", 15),
    # 空字符串（非法）
    ("\"", 1, True, "", 2),
    # 未终止的字符串（抛出异常）
    ("\"hello", 1, True, None, None),
    # 无引号的字符串（抛出异常）
    ("hello", 0, True, None, None),
    # 边界情况：单个字符
    ("\"a\"", 1, True, "a", 3),
    # 长字符串
    ("\"abcdefghijklmnopqrstuvwxyz\"", 1, True, "abcdefghijklmnopqrstuvwxyz", 28),
    # 包含换行符
    ("\"hello\nworld\"", 1, True, "hello\nworld", 14),
    # 包含多个转义字符
    ("\"hello\\\\\\\"world\"", 1, True, "hello\\\"world", 15),
    # 严格模式下非法转义
    ("\"hello\\xworld\"", 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None