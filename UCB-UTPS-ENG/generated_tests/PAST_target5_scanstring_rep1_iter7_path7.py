# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 1, 迭代: 7
# 生成时间: 2026-05-23 09:20:43

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符：双引号
    ('"he\\"llo"', 1, True, ['he"llo'], 7),
    # 转义字符：反斜杠
    ('"he\\llo"', 1, True, ['he\\llo'], 7),
    # 多个转义字符
    ('"he\\"l\\lo"', 1, True, ['he"l\\lo'], 8),
    # 字符串中包含多个非转义字符
    ('"abc123xyz"', 1, True, ['abc123xyz'], 9),
    # 空字符串（应抛出异常）
    ('"', 1, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"incomplete', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 边界情况：空字符串（不合法）
    ('""', 1, True, None, None),
    # 严格模式下非法转义
    ('"invalid\\x"', 1, True, None, None),
    # 非严格模式下允许非法转义
    ('"invalid\\x"', 1, False, ['invalid\\x'], 7),
    # 转义字符后紧跟其他字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 11),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, end_index = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert end_index == expected_end