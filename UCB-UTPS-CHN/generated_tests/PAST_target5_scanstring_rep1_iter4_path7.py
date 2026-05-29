# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 1, 迭代: 4
# 生成时间: 2026-04-18 16:39:41

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符：双引号
    ('"hello\\"world"', 1, True, ['hello"world'], 12),
    # 转义字符：反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 多个转义字符
    ('"hello\\"world\\\\test"', 1, True, ['hello"world\\test'], 15),
    # 空字符串（错误）
    ('""', 1, True, [], 1),
    # 未终止字符串（错误）
    ('"hello', 1, True, None, None),
    # 无引号（错误）
    ('hello"', 0, True, None, None),
    # 转义字符后没有内容（错误）
    ('"\\', 1, True, None, None),
    # 转义无效字符（错误）
    ('"\\x"', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"this is a long string with spaces and special characters: !@#$%^&*()"', 1, True, ['this is a long string with spaces and special characters: !@#$%^&*()'], 67),
    # 多次循环处理
    ('"a\\nb\\nc"', 1, True, ['a\nb\nc'], 8),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, end_index = scanstring(s, end, strict)
        parts = result.split('\n') if '\n' in result else [result]
        assert parts == expected_parts
        assert end_index == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None