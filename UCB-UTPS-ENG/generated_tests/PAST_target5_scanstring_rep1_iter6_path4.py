# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 1, 迭代: 6
# 生成时间: 2026-04-18 16:39:55

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 情况1: 正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 情况2: 字符串包含转义字符
    ('"he\\\"llo"', 1, True, ['he"llo'], 8),
    # 情况3: 字符串包含转义反斜杠
    ('"he\\\\llo"', 1, True, ['he\\llo'], 8),
    # 情况4: 字符串包含其他转义字符（模拟未处理的分支）
    ('"he\\x llo"', 1, True, ['he\\x llo'], 8),
    # 情况5: 空字符串（边界情况）
    ('""', 1, True, [''], 2),
    # 情况6: 未终止的字符串（异常情况）
    ('"unterminated', 1, True, None, None),
    # 情况7: 转义字符后没有内容（异常情况）
    ('"\\', 1, True, None, None),
    # 情况8: 多个转义字符
    ('"he\\\\\\\"llo"', 1, True, ['he\\\\"llo'], 10),
    # 情况9: 转义字符后有其他字符
    ('"he\\a llo"', 1, True, None, None),
    # 情况10: 长字符串
    ('"a" * 100', 1, True, ['a' * 100], 102),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, end_index = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected '{''.join(expected_parts)}', got '{result}'"
        assert end_index == expected_end, f"Expected end index {expected_end}, got {end_index}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Unexpected exception"