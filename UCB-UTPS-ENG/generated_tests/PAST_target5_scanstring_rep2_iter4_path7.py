# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 2, 迭代: 4
# 生成时间: 2026-04-18 16:41:52

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
    # 未闭合的字符串（应抛出异常）
    ('"hello', 1, True, None, None),
    # 空字符串（应抛出异常）
    ('""', 1, True, None, None),
    # 字符串中包含换行符
    ('"hello\nworld"', 1, True, ['hello\nworld'], 12),
    # 仅一个引号（应抛出异常）
    ('"', 1, True, None, None),
    # 有多个转义字符的复杂情况
    ('"a\\nb\\tc\\td"', 1, True, ['a\nb\tc\td'], 10),
    # 转义字符后没有内容（应抛出异常）
    ('"hello\\', 1, True, None, None),
    # 转义字符无效
    ('"hello\\x"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert final_end == expected_end, f"Expected end {expected_end}, got {final_end}"
    except ValueError as e:
        if expected_parts is None and expected_end is None:
            pass
        else:
            raise AssertionError(f"Unexpected exception: {e}")