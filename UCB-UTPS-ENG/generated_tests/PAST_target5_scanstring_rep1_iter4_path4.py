# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 1, 迭代: 4
# 生成时间: 2026-05-23 09:20:20

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
    # 字符串中包含其他转义字符（模拟省略部分）
    ('"hello\\\\nworld"', 1, True, ['hello\\nworld'], 12),
    # 空字符串（应抛出异常）
    ('""', 1, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"hello', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"abcdefghijklmnopqrstuvwxyz"', 1, True, ['abcdefghijklmnopqrstuvwxyz'], 28),
    # 包含多个转义字符的复杂字符串
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 转义字符后没有内容（仅转义）
    ('"\\\\"', 1, True, ['"'], 4),
    # 严格模式下，非法转义
    ('"hello\\x"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end