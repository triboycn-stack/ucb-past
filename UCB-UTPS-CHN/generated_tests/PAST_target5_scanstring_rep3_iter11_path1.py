# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 3, 迭代: 11
# 生成时间: 2026-04-18 16:44:26

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串被双引号包围
    ('"hello"', 0, True, ['hello'], 6),
    # 转义字符处理：转义双引号
    ('"he\\"llo"', 0, True, ['he"llo'], 8),
    # 转义字符处理：转义反斜杠
    ('"he\\\\llo"', 0, True, ['he\\llo'], 9),
    # 多个转义字符
    ('"he\\\\\\"llo"', 0, True, ['he\\"llo'], 10),
    # 无转义字符的字符串
    ('"world"', 0, True, ['world'], 6),
    # 字符串中间有转义
    ('"hello\\\\world"', 0, True, ['hello\\world'], 12),
    # 字符串中包含多个转义
    ('"a\\\\b\\\\\"c"', 0, True, ['a\\b\\"c'], 11),
    # 空字符串（错误情况）
    ('""', 0, True, ['', ''], 2),
    # 未终止的字符串（抛出异常）
    pytest.param('"hello', 0, True, None, None, marks=pytest.mark.xfail(raises=ValueError)),
    # 转义字符后没有内容（错误情况）
    pytest.param('"\\', 0, True, None, None, marks=pytest.mark.xfail(raises=ValueError)),
    # 无效转义字符（抛出异常）
    pytest.param('"h\\x"', 0, True, None, None, marks=pytest.mark.xfail(raises=ValueError)),
    # 边界情况：单个字符
    ('"a"', 0, True, ['a'], 3),
    # 长字符串
    ('"this is a very long string with many characters"', 0, True, ['this is a very long string with many characters'], 47),
    # 多次循环处理
    ('"a\\b\\c\\d"', 0, True, ['a\\b\\c\\d'], 9),
    # 严格模式下，非转义字符处理
    ('"abc"', 0, True, ['abc'], 4),
    # 非严格模式下，允许某些特殊字符（假设逻辑不同）
    ('"abc\\x"', 0, False, ['abc\\x'], 6),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, actual_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert actual_end == expected_end