# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 0, 迭代: 4
# 生成时间: 2026-05-23 09:19:22

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 情况1: 正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 情况2: 字符串中有转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 情况3: 转义字符后没有有效字符（错误情况）
    ('"hello\\"', 1, True, ['hello'], 7),
    # 情况4: 转义字符无效
    ('"hello\\x"', 1, True, ['hello'], 8),
    # 情况5: 空字符串（错误）
    ('"', 0, True, [], 1),
    # 情况6: 多个转义字符
    ('"a\\nb\\tc\\td"', 1, True, ['a\nb\tc\td'], 12),
    # 情况7: 字符串中包含多个未转义的字符
    ('"abcde"', 1, True, ['abcde'], 6),
    # 情况8: 字符串中包含转义字符但未正确结束
    ('"hello\\', 1, True, ['hello'], 7),
    # 情况9: 字符串中包含转义字符且严格模式
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 情况10: 字符串中包含转义字符但不合法
    ('"hello\\xworld"', 1, True, ['hello'], 9),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    result_str, result_end = scanstring(s, end, strict)
    assert result_str == ''.join(expected_parts)
    assert result_end == expected_end