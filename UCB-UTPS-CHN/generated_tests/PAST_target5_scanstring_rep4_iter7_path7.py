# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 4, 迭代: 7
# 生成时间: 2026-05-23 09:23:55

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello\"", 0, True, ["hello"], 6),
    # 转义字符：\" -> "
    ("hello\\\"", 0, True, ["hello\""], 7),
    # 多个转义字符
    ("hello\\\\world\"", 0, True, ["hello\\world"], 13),
    # 空字符串（非法）
    ("\"", 0, True, [], 1),
    # 未终止字符串（异常）
    ("hello", 0, True, [], None),
    # 边界情况：单个字符
    ("a\"", 0, True, ["a"], 2),
    # 多个转义字符处理
    ("a\\b\\c\"", 0, True, ["a\\b\\c"], 7),
    # 转义字符后没有引号（异常）
    ("abc\\", 0, True, [], None),
    # 转义字符无效
    ("abc\\x", 0, True, [], None),
    # 长字符串
    ("a" * 100 + "\"", 0, True, ["a" * 100], 101),
    # 转义字符在中间
    ("a\\b\"", 0, True, ["a\\b"], 5),
    # 转义字符在末尾
    ("a\\\"", 0, True, ["a\""], 4),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        parts = []
        current = end
        while current < len(s):
            if s[current] == '"':
                break
            if s[current] == '\\':
                current += 1
                if current >= len(s):
                    raise ValueError("Unterminated string")
                if s[current] == '"':
                    parts.append(s[end:current-1] + '"')
                    end = current + 1
                elif s[current] == '\\':
                    parts.append(s[end:current-1] + '\\')
                    end = current + 1
                else:
                    raise ValueError("Invalid escape")
                current += 1
            else:
                current += 1
        parts.append(s[end:current])
        assert ''.join(parts) == result
        assert actual_end == expected_end
    except ValueError as e:
        assert expected_end is None