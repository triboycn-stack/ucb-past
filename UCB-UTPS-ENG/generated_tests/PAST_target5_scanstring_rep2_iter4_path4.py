# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 2, 迭代: 4
# 生成时间: 2026-05-23 09:16:02

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后无内容
    ('"hello\\"', 1, True, ['hello"'], 8),
    # 字符串中包含多个非转义字符
    ('"abc def ghi"', 1, True, ['abc def ghi'], 12),
    # 空字符串（应抛出异常）
    ('""', 1, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"unclosed', 1, True, None, None),
    # 转义字符错误
    ('"invalid\\x"', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"a" * 100', 1, True, ['a' * 100], 102),
    # 转义字符在字符串中间
    ('"hello\\nworld"', 1, True, ['hello\nworld'], 13),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, result_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert result_end == expected_end