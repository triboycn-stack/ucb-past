# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 4, 迭代: 3
# 生成时间: 2026-04-18 16:45:13

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("\"hello world\"", 1, True, ["hello world"], 13),
    # 转义字符：双引号
    ("\"hello\\\"world\"", 1, True, ["hello\"world"], 14),
    # 转义字符：反斜杠
    ("\"hello\\\\world\"", 1, True, ["hello\\world"], 14),
    # 多个转义字符
    ("\"hello\\\\\\\"world\"", 1, True, ["hello\\\"world"], 15),
    # 空字符串（错误）
    ("\"", 1, True, [], 1),
    # 未终止字符串（错误）
    ("\"hello", 1, True, [], None),
    # 边界情况：单个字符
    ("\"a\"", 1, True, ["a"], 3),
    # 边界情况：多个字符
    ("\"abcde\"", 1, True, ["abcde"], 6),
    # 转义字符在字符串中间
    ("\"hello\\nworld\"", 1, True, ["hello\nworld"], 14),
    # 转义字符后无内容
    ("\"\\\"", 1, True, ["\""], 3),
    # 转义字符后有其他字符
    ("\"\\x\"", 1, True, ["x"], 4),
    # 错误转义字符
    ("\"\\z\"", 1, True, [], None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        parts = result.split('\n') if '\n' in result else [result]
        assert parts == expected_parts
        assert actual_end == expected_end
    except ValueError:
        assert expected_end is None