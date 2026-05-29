# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 3, 迭代: 14
# 生成时间: 2026-04-18 16:44:46

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ("hello", 0, True, ["hello"], 5),
    # 带转义字符的情况
    ('"hello\\"world"', 1, True, ['hello"world'], 12),
    # 转义字符为反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 多个转义字符
    ('"hello\\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"hello', 0, True, None, None),
    # 转义字符后没有内容（应抛出异常）
    ('"\\', 1, True, None, None),
    # 转义无效字符（应抛出异常）
    ('"\\x"', 1, True, None, None),
    # 字符串中包含多个转义
    ('"a\\nb\\tc\\rd\\fe"', 1, True, ['a\nb\tc\rd\fe'], 9),
    # 边界情况：字符串长度为1
    ('"a"', 1, True, ['a'], 2),
    # 边界情况：字符串为空（但被引号包围）
    ('""', 0, True, [''], 1),
    # 多次循环处理
    ('"abc\\def\\ghi"', 1, True, ['abc\ndef\ghi'], 11),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, end_index = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert end_index == expected_end, f"Expected end index {expected_end}, got {end_index}"
    except ValueError as e:
        assert expected_parts is None and expected_end is None, f"Expected exception, but got {e}"