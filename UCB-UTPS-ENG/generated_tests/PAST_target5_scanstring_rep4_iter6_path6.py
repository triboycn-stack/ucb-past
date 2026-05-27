# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 4, 迭代: 6
# 生成时间: 2026-05-23 09:23:47

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 正常情况：字符串以双引号结束
    ('"hello"', 0, True, 'hello', 6),
    # 转义字符处理：转义双引号
    ('"hello\\"world"', 0, True, 'hello"world', 13),
    # 转义字符处理：转义反斜杠
    ('"hello\\\\world"', 0, True, 'hello\\world', 13),
    # 多个转义字符
    ('"hello\\\\\\"world"', 0, True, 'hello\\"world', 14),
    # 字符串中间有普通字符
    ('"abc123"', 0, True, 'abc123', 7),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 未闭合的字符串（抛出异常）
    ('"unclosed', 0, True, None, None),
    # 边界情况：单个字符
    ('"a"', 0, True, 'a', 3),
    # 多次循环处理
    ('"a\\nb\\tc\\rd"', 0, True, 'a\nb\tc\rd', 10),
    # 严格模式下非法转义
    ('"invalid\\x"', 0, True, None, None),
    # 非严格模式下允许非法转义
    ('"invalid\\x"', 0, False, 'invalid\\x', 9),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None