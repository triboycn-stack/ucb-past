# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 3, 迭代: 9
# 生成时间: 2026-04-18 16:44:09

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基础情况：正常字符串，无转义
    ("hello\"world", 0, True, ["hello"], 5),
    # 转义字符处理
    ("hello\\\"world", 0, True, ["hello\""], 6),
    # 多个转义字符
    ("hello\\\\world", 0, True, ["hello\\"], 7),
    # 空字符串（非法）
    ("\"", 0, True, [], 1),
    # 未终止字符串（异常）
    ("hello", 0, True, [], -1),
    # 边界情况：字符串开始即为引号
    ("\"test", 0, True, [], 1),
    # 多次转义
    ("a\\b\\\"c", 0, True, ["a\\b\""], 5),
    # 长字符串
    ("a" * 100 + "\"", 0, True, ["a" * 100], 101),
    # 转义后继续处理
    ("abc\\ndef\"ghi", 0, True, ["abc\ndef"], 8),
])
def test_scanstring_core_logic(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
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
        expected_result = ''.join(parts)
        assert result == expected_result
        assert final_end == expected_end
    except ValueError as e:
        assert str(e) == "Unterminated string" and expected_end == -1