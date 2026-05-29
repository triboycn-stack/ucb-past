# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 4, 迭代: 12
# 生成时间: 2026-04-18 16:46:21

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
    ('"hello\\"world\\\\test"', 1, True, ['hello"world\\test'], 16),
    # 空字符串（错误）
    ('"', 0, True, [], 0),
    # 未终止的字符串（错误）
    ('"hello', 1, True, [], 1),
    # 转义字符后无内容（错误）
    ('"hello\\"', 1, True, [], 1),
    # 转义字符无效（错误）
    ('"hello\\x"', 1, True, [], 1),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"this is a long string with many characters"', 1, True, ['this is a long string with many characters'], 41),
    # 混合转义和普通字符
    ('"a\\nb\\tc\\td"', 1, True, ['a\nb\tc\td'], 12),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    parts = []
    begin = end
    while True:
        try:
            ch = s[end]
        except IndexError:
            raise ValueError("Unterminated string")
        if ch == '"':
            break
        if ch == '\\':
            # 转义处理
            end += 1
            try:
                esc = s[end]
            except IndexError:
                raise ValueError("Unterminated string")
            if esc == '"':
                parts.append(s[begin:end-1] + '"')
                begin = end + 1
            elif esc == '\\':
                parts.append(s[begin:end-1] + '\\')
                begin = end + 1
            else:
                raise ValueError("Invalid escape")
            end += 1
        else:
            end += 1
    parts.append(s[begin:end])
    result = ''.join(parts), end + 1
    assert result == ("".join(expected_parts), expected_end)