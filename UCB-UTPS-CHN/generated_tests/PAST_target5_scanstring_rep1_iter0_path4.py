# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 1, 迭代: 0
# 生成时间: 2026-04-18 16:39:13

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
    # 字符串未闭合（异常情况）
    ('"hello', 1, True, None, None),
    # 空字符串（异常情况）
    ('""', 1, True, [''], 2),
    # 转义字符无效
    ('"hello\\x"', 1, True, None, None),
    # 边界情况：单字符字符串
    ('"a"', 1, True, ['a'], 3),
    # 多次循环处理
    ('"a\\nb\\tc\\rd"', 1, True, ['a\nb\tc\rd'], 10),
    # 转义字符后紧跟其他字符
    ('"hello\\w"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result = scanstring(s, end, strict)
        assert result[0] == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result[0]}"
        assert result[1] == expected_end, f"Expected end {expected_end}, got {result[1]}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but no exception was raised"