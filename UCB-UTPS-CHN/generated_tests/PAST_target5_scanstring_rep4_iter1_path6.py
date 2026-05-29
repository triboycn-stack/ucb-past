# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 4, 迭代: 1
# 生成时间: 2026-04-18 16:45:00

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 基本情况：正常字符串，以双引号结束
    ("\"hello world\"", 1, True, "hello world", 13),
    # 转义字符处理：转义双引号
    ("\"hello \\\"world\"", 1, True, "hello \"world", 14),
    # 转义字符处理：转义反斜杠
    ("\"hello \\\\world\"", 1, True, "hello \\world", 14),
    # 多个转义字符
    ("\"hello \\\\ \\\"world\"", 1, True, "hello \\ \"world", 16),
    # 空字符串（应抛出异常）
    ("\"", 1, True, None, None),
    # 未终止的字符串（end超出范围）
    ("\"hello", 1, True, None, None),
    # 边界情况：单个字符
    ("\"a\"", 1, True, "a", 3),
    # 边界情况：空字符串（仅双引号）
    ("\"\"", 1, True, "", 2),
    # 非双引号结束（应抛出异常）
    ("\"hello world", 1, True, None, None),
    # 严格模式下，非双引号结束抛出异常
    ("\"hello world", 1, True, None, None),
    # 非严格模式下，允许非双引号结束（但实际代码中仍会抛出异常）
    ("\"hello world", 1, False, None, None),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None