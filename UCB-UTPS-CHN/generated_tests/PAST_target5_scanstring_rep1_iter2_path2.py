# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 1, 迭代: 2
# 生成时间: 2026-05-23 09:20:05

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符处理
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后没有结束引号（异常）
    ('"hello\\', 1, True, [], -1),
    # 空字符串（异常）
    ('"', 0, True, [], -1),
    # 字符串中间有转义
    ('"h\\\"e\\\"l\\\"o"', 1, True, ['h"e"l"o'], 11),
    # 边界情况：字符串开始于索引0
    ('"test"', 0, True, ['test'], 5),
    # 转义字符后无内容
    ('"\\\\"', 1, True, ['"'], 3),
    # 转义字符后有其他字符
    ('"a\\\"b"', 1, True, ['a"b'], 6),
    # 转义字符错误
    ('"a\\x"', 1, True, [], -1),
    # 多次循环处理
    ('"a\\\"b\\\"c"', 1, True, ['a"b"c'], 9),
    # 转义字符在字符串中间
    ('"abc\\\"def"', 1, True, ['abc"def'], 10),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end
    except ValueError:
        assert expected_end == -1