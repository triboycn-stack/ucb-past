# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 0, 迭代: 11
# 生成时间: 2026-04-18 16:38:07

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串被双引号包围
    ('"hello"', 0, True, ['hello'], 6),
    # 转义字符处理：\" -> "
    ('"he\\\"llo"', 0, True, ['he"llo'], 8),
    # 多个转义字符
    ('"he\\\\llo"', 0, True, ['he\\llo'], 8),
    # 未终止字符串（触发异常）
    ('"hello', 0, True, None, None),
    # 空字符串（触发异常）
    ('"', 0, True, None, None),
    # 字符串中间有转义字符
    ('"h\\ne\\tst"', 0, True, ['h\ne\tst'], 9),
    # 多个转义字符和普通字符混合
    ('"a\\b\\nc\\td"', 0, True, ['a\b\nc\td'], 10),
    # 边界情况：字符串只有一个字符
    ('"x"', 0, True, ['x'], 3),
    # 边界情况：字符串长度为0（触发异常）
    ('""', 0, True, None, None),
    # 非法转义字符（触发异常）
    ('"he\\xlo"', 0, True, None, None),
    # 转义字符后没有字符（触发异常）
    ('"he\\\\"', 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end