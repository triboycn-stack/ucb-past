# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 2, 迭代: 2
# 生成时间: 2026-05-23 09:21:07

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 转义字符错误
    ('"hello\\x"', 1, True, None, None),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 空字符串（非法）
    ('""', 1, True, None, None),
    # 未终止的字符串（抛出异常）
    ('"hello', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 转义后继续处理
    ('"a\\nb"', 1, True, ['a\nb'], 5),
    # 多次循环处理
    ('"a\\\"b\\\"c"', 1, True, ['a"b"c'], 9),
    # 严格模式下不支持转义
    ('"a\\b"', 1, True, None, None),
    # 非严格模式下允许转义
    ('"a\\b"', 1, False, ['a\\b'], 5),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end {expected_end}, got {new_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but no exception was raised"