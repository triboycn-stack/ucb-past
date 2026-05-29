# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 3, 迭代: 7
# 生成时间: 2026-05-23 09:22:56

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串中包含转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 正常情况：字符串中没有转义字符
    ('"hello world"', 1, True, ['hello world'], 12),
    # 转义字符处理：转义双引号
    ('"hello\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 转义字符处理：转义反斜杠
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 15),
    # 异常情况：未终止的字符串（索引越界）
    ('"hello', 1, True, None, None),
    # 异常情况：无效转义字符
    ('"hello\\xworld"', 1, True, None, None),
    # 边界情况：空字符串
    ('""', 1, True, [''], 2),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 循环测试：多个字符
    ('"abcde"', 1, True, ['abcde'], 6),
    # 循环测试：多个转义字符
    ('"a\\\\b\\\\\"c"', 1, True, ['a\\b"c'], 9),
    # 条件分支测试：ch != '"'
    ('"abc"def', 1, True, ['abc'], 4),
    # 条件分支测试：ch == '"'
    ('"abc"', 1, True, ['abc'], 4),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None