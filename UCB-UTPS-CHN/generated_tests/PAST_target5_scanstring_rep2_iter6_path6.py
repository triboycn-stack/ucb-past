# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 2, 迭代: 6
# 生成时间: 2026-05-23 09:16:17

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
    ("\"hello\\\\\\\"world\"", 1, True, "hello\\\\\"world", 15),
    # 空字符串（非法）
    ("\"", 1, True, "", 2),
    # 未终止的字符串（抛出异常）
    ("\"hello", 1, True, None, None),
    # 边界情况：单个字符
    ("\"a\"", 1, True, "a", 3),
    # 多次循环处理
    ("\"abc\\\"def\\\\ghi\"", 1, True, "abc\"def\\ghi", 16),
    # 严格模式下，非法转义字符
    ("\"hello\\xworld\"", 1, True, None, None),
    # 非严格模式下，允许非法转义字符
    ("\"hello\\xworld\"", 1, False, "hello\\xworld", 11),
    # 无转义字符
    ("\"abcdefg\"", 1, True, "abcdefg", 9),
    # 字符串中包含换行符
    ("\"hello\nworld\"", 1, True, "hello\nworld", 12),
    # 字符串中包含制表符
    ("\"hello\tworld\"", 1, True, "hello\tworld", 12),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError as e:
        assert expected_value is None and expected_end is None
        assert str(e) == "Invalid escape" if "Invalid escape" in str(e) else "Unterminated string" in str(e)