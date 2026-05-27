# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 2, 迭代: 0
# 生成时间: 2026-04-18 16:41:05

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello", 0, True, ["hello"], 5),
    # 转义字符处理
    ("h\\\"ello", 0, True, ["h\"ello"], 6),
    # 多个转义字符
    ("h\\\\\"ello", 0, True, ["h\\\"ello"], 7),
    # 转义字符后无结束引号（异常）
    ("h\\\"", 0, True, [], None),
    # 空字符串（异常）
    ("", 0, True, [], None),
    # 仅一个引号（异常）
    ('"', 0, True, [], None),
    # 转义字符后非有效字符（异常）
    ("h\\x", 0, True, [], None),
    # 多次循环处理
    ("a\\b\\c\"", 0, True, ["a\\b\\c\""], 6),
    # 边界情况：字符串长度为1
    ('"', 0, True, [], None),
    # 字符串中间有转义
    ("\\\"test\"", 0, True, ['\"test"'], 7),
    # 长字符串
    ("a" * 100 + "\"", 0, True, ["a" * 100], 101),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        parts = []
        current = 0
        while current < len(result):
            if result[current] == '\\':
                parts.append(result[current:current+2])
                current += 2
            else:
                parts.append(result[current])
                current += 1
        assert parts == expected_parts
        assert actual_end == expected_end
    except ValueError:
        assert expected_end is None