# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 2, 迭代: 2
# 生成时间: 2026-05-23 09:15:49

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 测试带转义字符的字符串
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 测试转义字符为反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 测试转义字符为其他字符（抛出异常）
    ('"hello\\xworld"', 1, True, None, None),
    # 测试字符串未闭合（抛出异常）
    ('"hello', 1, True, None, None),
    # 测试空字符串（抛出异常）
    ('"', 1, True, None, None),
    # 测试多个转义字符
    ('"a\\\"b\\\\c"', 1, True, ['a"b\\c'], 11),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 测试转义字符后无内容
    ('"\\\\"', 1, True, ['\\'], 4),
    # 测试转义字符后有内容
    ('"\\\"test"', 1, True, ['"test'], 7),
    # 测试转义字符后有多个字符
    ('"\\\"test\\\"end"', 1, True, ['"test"end'], 12),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None