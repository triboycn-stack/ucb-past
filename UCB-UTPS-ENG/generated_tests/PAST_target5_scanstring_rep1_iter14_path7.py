# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 1, 迭代: 14
# 生成时间: 2026-04-18 16:40:58

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串包含转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 正常情况：字符串无转义字符
    ('"hello world"', 1, True, ['hello world'], 12),
    # 转义字符处理：反斜杠后是双引号
    ('"hello\\\\\"world"', 1, True, ['hello\\"world'], 13),
    # 转义字符处理：反斜杠后是反斜杠
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 转义字符处理：非法转义
    ('"hello\\xworld"', 1, True, None, None),
    # 字符串未闭合（触发异常）
    ('"hello', 1, True, None, None),
    # 空字符串（触发异常）
    ('"', 1, True, None, None),
    # 多个转义字符
    ('"a\\\\b\\\"c\\\\d"', 1, True, ['a\\b"c\\d'], 13),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 边界情况：空字符串（但有引号）
    ('"', 0, True, None, None),
    # 非法输入：s不是字符串
    (12345, 0, True, None, None),
    # 非法输入：end不是整数
    ('"hello"', 'abc', True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end