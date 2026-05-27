# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 1, 迭代: 1
# 生成时间: 2026-05-23 09:19:58

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串被正确解析
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 转义字符错误
    ('"hello\\"', 1, True, None, None),
    # 字符串未闭合
    ('"hello', 1, True, None, None),
    # 空字符串
    ('""', 1, True, [''], 2),
    # 多个转义字符
    ('"a\\\\b\\\"c"', 1, True, ['a\\b"c'], 9),
    # 边界情况：字符串长度为1
    ('"a"', 1, True, ['a'], 3),
    # 转义字符后无字符
    ('"\\', 1, True, None, None),
    # 转义字符无效
    ('"\\x"', 1, True, None, None),
    # 多次转义
    ('"\\\\\\\\"', 1, True, ['\\\\'], 6),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end {expected_end}, got {new_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but got result"