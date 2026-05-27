# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 2, 迭代: 1
# 生成时间: 2026-05-23 09:15:42

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 正常情况：字符串被正确解析
    ('"hello"', 1, True, 'hello', 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, 'hello"world', 13),
    # 转义字符错误的情况
    ('"hello\\x"', 1, True, None, None),
    # 字符串未闭合（抛出异常）
    ('"hello', 1, True, None, None),
    # 空字符串（抛出异常）
    ('"', 1, True, None, None),
    # 多个转义字符
    ('"a\\nb\\tc\\rd"', 1, True, 'a\nb\td\r', 9),
    # 边界情况：字符串只有一个字符
    ('"a"', 1, True, 'a', 3),
    # 转义字符后没有内容
    ('"\\\\"', 1, True, '"', 4),
    # 转义字符后有其他字符
    ('"\\x"', 1, True, None, None),
    # 复杂转义组合
    ('"\\\"\\\\\\n\\r\\t"', 1, True, '"\\\n\r\t', 12),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None