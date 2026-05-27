# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 2, 迭代: 12
# 生成时间: 2026-04-18 16:42:48

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
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 未终止的字符串（索引越界）
    ('"hello', 0, True, None, None),
    # 无转义字符的普通字符串
    ('"world"', 0, True, 'world', 7),
    # 字符串中间有其他字符
    ('"abc123"', 0, True, 'abc123', 8),
    # 边界情况：单个字符
    ('"a"', 0, True, 'a', 3),
    # 长字符串
    ('"abcdefghijklmnopqrstuvwxyz"', 0, True, 'abcdefghijklmnopqrstuvwxyz', 29),
    # 转义字符在字符串中间
    ('"hello\\\\world"', 0, True, 'hello\\world', 13),
    # 转义字符后没有内容
    ('"\\', 0, True, None, None),
    # 转义字符无效
    ('"\\x"', 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError as e:
        assert expected_value is None and expected_end is None
        assert str(e) == "Unterminated string" or str(e) == "Invalid escape"