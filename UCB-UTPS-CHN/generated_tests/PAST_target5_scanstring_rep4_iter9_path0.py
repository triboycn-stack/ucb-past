# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 4, 迭代: 9
# 生成时间: 2026-04-18 16:46:00

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符 \"
    ('"hello\\"world"', 1, True, ['hello"world'], 12),
    # 转义字符 \\
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 多个转义字符
    ('"hello\\\\\\"world"', 1, True, ['hello\\"world'], 13),
    # 空字符串（错误情况）
    ('""', 1, True, [], 1),
    # 未终止的字符串（错误情况）
    ('"hello', 1, True, [], None),
    # 转义字符后没有内容（错误情况）
    ('"\\', 1, True, [], None),
    # 转义字符后无效字符（错误情况）
    ('"\\x"', 1, True, [], None),
    # 多次循环处理
    ('"a\\nb\\tc"', 1, True, ['a\nb\tc'], 7),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"this is a long string with many characters and escape \\\"."', 1, True, ['this is a long string with many characters and escape "'], 48),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert actual_end == expected_end
    except ValueError as e:
        assert expected_end is None
        assert "Unterminated string" in str(e) or "Invalid escape" in str(e)