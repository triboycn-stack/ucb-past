# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 2, 迭代: 2
# 生成时间: 2026-04-18 16:41:40

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
    ('"h\\ne\\tlo"', 0, True, ['h\ne\tlo'], 9),
    # 非双引号结束（触发异常）
    ('"hello world', 0, True, None, None),
    # 边界情况：单个字符
    ('"a"', 0, True, ['a'], 3),
    # 多次循环处理
    ('"abc\\ndef\\tghi"', 0, True, ['abc\ndef\tghi'], 12),
    # 转义字符后无内容（触发异常）
    ('"\\', 0, True, None, None),
    # 转义字符后无效字符（触发异常）
    ('"\\x"', 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end