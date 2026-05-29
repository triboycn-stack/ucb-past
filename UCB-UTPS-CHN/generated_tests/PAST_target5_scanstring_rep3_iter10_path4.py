# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 3, 迭代: 10
# 生成时间: 2026-04-18 16:44:18

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 情况1: 正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 情况2: 字符串包含转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 情况3: 字符串包含转义字符但未正确结束
    ('"hello\\', 1, True, [], -1),
    # 情况4: 空字符串（非法）
    ('"', 0, True, [], -1),
    # 情况5: 字符串包含多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 14),
    # 情况6: 字符串包含转义字符但无效
    ('"hello\\x"', 1, True, [], -1),
    # 情况7: 字符串包含多个正常字符
    ('"abc def ghi"', 1, True, ['abc def ghi'], 13),
    # 情况8: 字符串包含换行符
    ('"hello\nworld"', 1, True, ['hello\nworld'], 13),
    # 情况9: 字符串包含转义字符和正常字符
    ('"hello\\nworld"', 1, True, ['hello\nworld'], 13),
    # 情况10: 字符串以转义字符结尾（非法）
    ('"hello\\"', 1, True, [], -1),
    # 情况11: 字符串包含多个转义字符
    ('"a\\nb\\tc\\td"', 1, True, ['a\nb\tc\td'], 12),
    # 情况12: 字符串包含转义字符和正常字符混合
    ('"a\\\"b\\nc"', 1, True, ['a"b\nc'], 10),
    # 情况13: 字符串包含转义字符但未正确处理
    ('"hello\\', 1, True, [], -1),
    # 情况14: 字符串包含转义字符但超出范围
    ('"hello\\x"', 1, True, [], -1),
    # 情况15: 字符串包含多个转义字符和正常字符
    ('"a\\\"b\\\"c"', 1, True, ['a"b"c'], 10),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        parts = result.split('\n') if '\n' in result else [result]
        assert parts == expected_parts
        assert final_end == expected_end
    except ValueError as e:
        assert str(e) == "Unterminated string"
        assert expected_end == -1