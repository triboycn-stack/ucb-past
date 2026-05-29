# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 0, 迭代: 5
# 生成时间: 2026-04-18 16:37:26

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 带有转义字符的字符串
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后没有内容（错误）
    ('"hello\\"', 1, True, ['hello'], 7),
    # 字符串未闭合（错误）
    ('"hello', 1, True, [], -1),
    # 空字符串（错误）
    ('"', 1, True, [], -1),
    # 仅转义字符（错误）
    ('"\\', 1, True, [], -1),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"abcdefghijklmnopqrstuvwxyz"', 1, True, ['abcdefghijklmnopqrstuvwxyz'], 28),
    # 转义字符在中间
    ('"h\\\"ello"', 1, True, ['h"ello'], 9),
    # 转义字符在末尾
    ('"hello\\\""', 1, True, ['hello"'], 9),
    # 多个转义字符
    ('"h\\\\\\\"ello"', 1, True, ['h\\\\"ello'], 10),
    # 转义字符后无效字符（错误）
    ('"hello\\x"', 1, True, [], -1),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        parts = result.split('\n') if '\n' in result else [result]
        assert parts == expected_parts
        assert final_end == expected_end
    except ValueError as e:
        assert expected_end == -1
        assert str(e) == "Unterminated string" or str(e) == "Invalid escape"