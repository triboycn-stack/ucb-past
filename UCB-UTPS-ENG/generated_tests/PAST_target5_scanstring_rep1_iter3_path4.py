# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 1, 迭代: 3
# 生成时间: 2026-04-18 16:39:34

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
    ('"hello\\"', 1, True, ['hello"'], 8),
    # 未正确转义
    ('"hello\\x"', 1, True, None, None),
    # 未闭合的字符串
    ('"hello', 1, True, None, None),
    # 空字符串
    ('""', 1, True, [''], 2),
    # 字符串中间有换行
    ('"hello\nworld"', 1, True, ['hello\nworld'], 12),
    # 多次进入转义逻辑
    ('"a\\nb\\nc"', 1, True, ['a\nb\nc'], 9),
    # 边界情况：字符串长度为1
    ('"a"', 1, True, ['a'], 2),
    # 非法输入：end超出范围
    ('"abc"', 10, True, None, None),
    # 非法输入：s为空
    ('', 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts: {expected_parts}, got: {result}"
        assert new_end == expected_end, f"Expected end: {expected_end}, got: {new_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected no exception but got one"