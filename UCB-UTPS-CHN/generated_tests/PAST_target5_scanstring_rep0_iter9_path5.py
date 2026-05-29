# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 0, 迭代: 9
# 生成时间: 2026-04-18 16:37:54

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串被双引号包围
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符：\" -> "
    ('"hello\\"world"', 1, True, ['hello"world'], 13),
    # 转义字符：\\ -> \
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 多个转义字符
    ('"hello\\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 未终止字符串（触发异常）
    ('"hello', 1, True, None, None),
    # 空字符串（触发异常）
    ('"', 1, True, None, None),
    # 字符串中间有转义但不匹配
    ('"hello\\x"', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 多次循环：多个非转义字符
    ('"abcde"', 1, True, ['abcde'], 6),
    # 多次循环：混合转义和非转义
    ('"a\\b"c', 1, True, ['a"b', 'c'], 6),
    # 严格模式下，非法转义抛出异常
    ('"hello\\x"', 1, True, None, None),
    # 非严格模式下，允许非法转义
    ('"hello\\x"', 1, False, ['hello\\x'], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert final_end == expected_end, f"Expected end index {expected_end}, got {final_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but got no exception"