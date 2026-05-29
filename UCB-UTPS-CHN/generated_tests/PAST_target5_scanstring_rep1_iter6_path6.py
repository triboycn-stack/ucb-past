# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 1, 迭代: 6
# 生成时间: 2026-05-23 09:20:35

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 基本情况：正常字符串，以双引号结束
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
    # 包含换行符的字符串
    ('"hello\nworld"', 0, True, 'hello\nworld', 12),
    # 包含多个转义字符的字符串
    ('"hello\\\\\\"world"', 0, True, 'hello\\"world', 14),
    # 边界情况：字符串长度为1
    ('"a"', 0, True, 'a', 3),
    # 边界情况：字符串为空（但包含双引号）
    ('""', 0, True, '', 2),
    # 错误处理：无效转义字符
    ('"hello\\x"', 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, end_index = scanstring(s, end, strict)
        assert value == expected_value
        assert end_index == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None