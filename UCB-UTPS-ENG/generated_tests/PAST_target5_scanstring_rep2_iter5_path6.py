# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 2, 迭代: 5
# 生成时间: 2026-04-18 16:41:59

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 转义字符错误
    ('"hello\\x"', 1, True, None, None),
    # 字符串未闭合（异常）
    ('"hello', 1, True, None, None),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 14),
    # 空字符串（异常）
    ('"', 1, True, None, None),
    # 转义后没有字符（异常）
    ('"\\', 1, True, None, None),
    # 多次循环处理
    ('"a\\nb\\tc\\rd"', 1, True, ['a\nb\tc\rd'], 10),
    # 边界情况：单字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"abcdefghijklmnopqrstuvwxyz"', 1, True, ['abcdefghijklmnopqrstuvwxyz'], 28),
    # 转义字符在中间
    ('"a\\tb"', 1, True, ['a\tb'], 6),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end