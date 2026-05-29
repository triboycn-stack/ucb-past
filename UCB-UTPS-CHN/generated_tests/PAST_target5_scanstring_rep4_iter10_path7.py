# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 4, 迭代: 10
# 生成时间: 2026-04-18 16:46:07

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 正常情况：字符串被正确解析
    ('"hello"', 0, True, 'hello', 6),
    # 转义字符处理：\" 被正确解析
    ('"he\\\"llo"', 0, True, 'he"llo', 8),
    # 多个转义字符
    ('"he\\\\llo"', 0, True, 'he\\llo', 8),
    # 字符串中间有普通字符
    ('"hello world"', 0, True, 'hello world', 13),
    # 空字符串（应抛出异常）
    ('""', 0, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"hello', 0, True, None, None),
    # 未闭合的字符串（边界条件）
    ('"hello', 5, True, None, None),
    # 转义字符后没有内容（应抛出异常）
    ('"\\', 0, True, None, None),
    # 转义字符后无效（应抛出异常）
    ('"\\x"', 0, True, None, None),
    # 多个转义字符处理
    ('"he\\\\\\\"llo"', 0, True, 'he\\\\"llo', 11),
    # 循环多次处理
    ('"a\\nb\\nc"', 0, True, 'a\nb\nc', 9),
    # 边界情况：字符串长度为1
    ('"a"', 0, True, 'a', 2),
    # 边界情况：字符串长度为0（应抛出异常）
    ('""', 0, True, None, None),
    # 非法输入：s不是字符串
    (12345, 0, True, None, None),
    # 非法输入：end不是整数
    ('"hello"', '0', True, None, None),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == expected_value
        assert new_end == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None