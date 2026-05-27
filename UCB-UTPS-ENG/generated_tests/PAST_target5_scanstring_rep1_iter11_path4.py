# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 1, 迭代: 11
# 生成时间: 2026-04-18 16:40:36

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 情况1: 正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 情况2: 字符串包含转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 情况3: 转义字符后没有有效字符（错误情况）
    ('"hello\\"', 1, True, ['hello'], 7),
    # 情况4: 转义字符无效
    ('"hello\\x"', 1, True, ['hello\\x'], 8),
    # 情况5: 空字符串（错误情况）
    ('""', 1, True, ['', 1], 2),
    # 情况6: 字符串未闭合（错误情况）
    ('"hello', 1, True, None, None),
    # 情况7: 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 14),
    # 情况8: 字符串中包含换行符
    ('"hello\nworld"', 1, True, ['hello\nworld'], 13),
    # 情况9: 字符串中包含多个转义字符
    ('"hello\\\\\"world"', 1, True, ['hello\\"world'], 15),
    # 情况10: 字符串中包含转义字符但未正确处理
    ('"hello\\', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        assert result == expected_parts
        assert actual_end == expected_end
    except ValueError as e:
        assert expected_parts is None and expected_end is None
        assert str(e) == "Unterminated string" or "Invalid escape" in str(e)