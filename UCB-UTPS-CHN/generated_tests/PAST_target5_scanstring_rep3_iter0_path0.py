# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 3, 迭代: 0
# 生成时间: 2026-05-23 09:22:01

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 测试带转义字符的字符串
    ('"he\\llo"', 1, True, ['he\\llo'], 7),
    # 测试转义字符为反斜杠的情况
    ('"he\\\\llo"', 1, True, ['he\\\\llo'], 8),
    # 测试多个转义字符
    ('"he\\\\\\\"llo"', 1, True, ['he\\\\\\\"llo'], 10),
    # 测试空字符串（应抛出异常）
    ('"', 0, True, [], 0),
    # 测试未终止的字符串（应抛出异常）
    ('"hello', 1, True, [], 1),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 测试多部分拼接
    ('"part1\\\"part2"', 1, True, ['part1\\"part2'], 11),
    # 测试转义字符后继续处理
    ('"abc\\ndef"', 1, True, ['abc\\ndef'], 8),
    # 测试转义字符后有其他字符
    ('"abc\\\\def"', 1, True, ['abc\\\\def'], 9),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert final_end == expected_end
    except ValueError as e:
        if expected_parts or expected_end:
            raise AssertionError(f"Unexpected exception: {e}")