# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 0, 迭代: 7
# 生成时间: 2026-05-23 09:19:42

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 0, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 0, True, ['hello"world'], 13),
    # 多个转义字符
    ('"hello\\\\world"', 0, True, ['hello\\world'], 13),
    # 转义字符后没有内容
    ('"hello\\\\"', 0, True, ['hello"'], 9),
    # 字符串中间有转义
    ('"hello\\nworld"', 0, True, ['hello\nworld'], 12),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"hello', 0, True, None, None),
    # 无效转义字符
    ('"hello\\x"', 0, True, None, None),
    # 边界情况：单个字符
    ('"a"', 0, True, ['a'], 3),
    # 长字符串
    ('"a" * 100', 0, True, ['a' * 100], 202),
    # 混合普通字符和转义
    ('"hello\\\"world\\n"', 0, True, ['hello"world\n'], 15),
    # 无转义但多个字符
    ('"abcde"', 0, True, ['abcde'], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end index {expected_end}, got {new_end}"
    except ValueError as e:
        assert expected_parts is None and expected_end is None, f"Unexpected error: {e}"