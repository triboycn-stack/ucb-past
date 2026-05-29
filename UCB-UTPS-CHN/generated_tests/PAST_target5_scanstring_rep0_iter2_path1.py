# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 0, 迭代: 2
# 生成时间: 2026-04-18 16:37:05

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 转义字符错误
    ('"hello\\xworld"', 1, True, None, None),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 未闭合的字符串
    ('"hello', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"abcdefghijklmnopqrstuvwxyz"', 1, True, ['abcdefghijklmnopqrstuvwxyz'], 27),
    # 包含多个转义字符
    ('"a\\nb\\tc\\rd\\fe"', 1, True, ['a\nb\tc\rd\fe'], 14),
    # 严格模式下非法转义
    ('"hello\\xworld"', 1, True, None, None),
    # 非严格模式下允许非法转义
    ('"hello\\xworld"', 1, False, ['hello\\xworld'], 12),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert actual_end == expected_end, f"Expected end {expected_end}, got {actual_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected no exception but got one"