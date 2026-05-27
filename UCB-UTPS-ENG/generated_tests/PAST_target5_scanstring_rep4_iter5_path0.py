# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 4, 迭代: 5
# 生成时间: 2026-04-18 16:45:26

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符 \"
    ('"hello\\"world"', 1, True, ['hello"world'], 12),
    # 转义字符 \\
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 多个转义字符
    ('"hello\\\\\\"world"', 1, True, ['hello\\"world'], 13),
    # 空字符串（错误情况）
    ('""', 1, True, [], 1),
    # 未终止的字符串（错误情况）
    ('"hello', 1, True, [], 1),
    # 转义字符后无内容（错误情况）
    ('"\\', 1, True, [], 1),
    # 转义字符无效（错误情况）
    ('"\\x"', 1, True, [], 1),
    # 多次循环处理
    ('"a\\nb\\tc\\td"', 1, True, ['a\nb\tc\td'], 9),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 边界情况：长字符串
    ('"abcdefghijklmnopqrstuvwxyz"', 1, True, ['abcdefghijklmnopqrstuvwxyz'], 27),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    result = scanstring(s, end, strict)
    assert isinstance(result, tuple)
    assert len(result) == 2
    value, final_end = result
    assert value == ''.join(expected_parts)
    assert final_end == expected_end