# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 0, 迭代: 13
# 生成时间: 2026-04-18 16:38:53

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后无内容
    ('"hello\\"', 1, True, ['hello"'], 7),
    # 转义字符错误
    ('"hello\\x"', 1, True, None, None),
    # 字符串未闭合（抛出异常）
    ('"hello', 1, True, None, None),
    # 空字符串（抛出异常）
    ('"', 1, True, None, None),
    # 转义字符后没有字符（抛出异常）
    ('"hello\\', 1, True, None, None),
    # 多个转义字符处理
    ('"hello\\\\\\\"world"', 1, True, ['hello\\\\"world'], 15),
    # 边界情况：单字符字符串
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"this is a very long string with many characters"', 1, True, ['this is a very long string with many characters'], 45),
    # 转义字符在中间
    ('"hello\\nworld"', 1, True, ['hello\nworld'], 12),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert actual_end == expected_end, f"Expected end index {expected_end}, got {actual_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but no exception was raised"