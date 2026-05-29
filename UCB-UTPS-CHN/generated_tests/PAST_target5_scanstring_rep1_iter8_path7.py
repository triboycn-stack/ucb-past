# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 1, 迭代: 8
# 生成时间: 2026-04-18 16:40:09

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后无内容
    ('"hello\\"', 1, True, ['hello"'], 8),
    # 转义字符错误
    ('"hello\\x"', 1, True, None, None),
    # 字符串未闭合（应抛出异常）
    ('"hello', 1, True, None, None),
    # 空字符串（应抛出异常）
    ('"', 1, True, None, None),
    # 长字符串
    ('"a" * 100', 1, True, ['a' * 100], 1 + len('a' * 100) + 1),
    # 边界情况：字符串开始于索引0
    ('"test"', 0, True, ['test'], 5),
    # 字符串中间有多个非转义字符
    ('"abc def ghi"', 1, True, ['abc def ghi'], 12),
    # 字符串中包含换行符
    ('"hello\nworld"', 1, True, ['hello\nworld'], 13),
    # 转义字符后是其他字符（应抛出异常）
    ('"hello\\x"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts: {expected_parts}, got: {result}"
        assert new_end == expected_end, f"Expected end: {expected_end}, got: {new_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected no exception but got one"