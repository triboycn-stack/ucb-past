# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 2, 迭代: 9
# 生成时间: 2026-04-18 16:42:27

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符处理
    ('"he\\\"llo"', 1, True, ['he"llo'], 7),
    # 多个转义字符
    ('"he\\\\llo"', 1, True, ['he\\llo'], 7),
    # 转义字符后没有结束引号（错误情况）
    ('"he\\', 1, True, [], -1),
    # 空字符串（错误情况）
    ('"', 1, True, [], -1),
    # 字符串中包含多个转义
    ('"h\\\"e\\\\l\\\"o"', 1, True, ['h"e\\l"o'], 9),
    # 边界情况：字符串开始于引号
    ('"a"', 1, True, ['a'], 2),
    # 长字符串
    ('"this is a very long string with many characters and some \\\"escapes\\"."', 1, True, ['this is a very long string with many characters and some "escapes"'], 48),
    # 错误转义字符
    ('"he\\xlo"', 1, True, [], -1),
    # 转义字符在字符串中间
    ('"hello\\nworld"', 1, True, ['hello\nworld'], 10),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        parts = result.split('\n') if '\n' in result else [result]
        assert parts == expected_parts
        assert final_end == expected_end
    except ValueError as e:
        assert expected_end == -1
        assert str(e) == "Invalid escape" if "Invalid escape" in str(e) else "Unterminated string" if "Unterminated string" in str(e) else "Unknown error"