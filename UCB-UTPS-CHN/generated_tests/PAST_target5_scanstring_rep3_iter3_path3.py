# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '"'
# 重复次数: 3, 迭代: 3
# 生成时间: 2026-05-23 09:22:22

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常情况：字符串中包含转义字符 \" 
    ('"hello\"world"', 1, True, ['hello"world'], 12),
    # 测试转义字符 \" 的情况
    ('"hello\\"world"', 1, True, ['hello"world'], 13),
    # 测试转义字符 \\ 的情况
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 测试空字符串（应抛出异常）
    ('"', 1, True, None, None),
    # 测试未终止的字符串（应抛出异常）
    ('"hello', 1, True, None, None),
    # 测试转义字符无效的情况（应抛出异常）
    ('"hello\\x"', 1, True, None, None),
    # 测试多个转义字符
    ('"hello\\\"world\\\\test"', 1, True, ['hello"world\\test'], 17),
    # 测试字符串中间有多个转义字符
    ('"a\\nb\\tc\\td"', 1, True, ['a\nb\tc\td'], 10),
    # 测试边界情况：字符串长度为1
    ('"a"', 1, True, ['a'], 2),
    # 测试字符串中有多个转义字符
    ('"a\\\\b\\\\c"', 1, True, ['a\\b\\c'], 9),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end