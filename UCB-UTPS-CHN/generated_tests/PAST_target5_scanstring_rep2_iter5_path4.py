# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 2, 迭代: 5
# 生成时间: 2026-05-23 09:21:29

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ("hello", 0, True, ["hello"], 5),
    # 带空格和换行的字符串
    ("  hello\n    world", 0, True, ["  hello\n    world"], 14),
    # 带转义字符的情况
    ("hello\\\"world", 0, True, ["hello\"world"], 12),
    # 转义字符后接其他字符
    ("hello\\\\world", 0, True, ["hello\\world"], 11),
    # 多个转义字符
    ("hello\\\\\"world", 0, True, ["hello\\\"world"], 13),
    # 空字符串（应抛出异常）
    ("", 0, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ("hello", 0, True, None, None),
    # 边界情况：单个字符
    ("a", 0, True, ["a"], 1),
    # 长字符串
    ("a" * 100, 0, True, ["a" * 100], 100),
    # 转义字符在中间
    ("h\\el\\lo", 0, True, ["h\\el\\lo"], 7),
    # 转义字符在末尾
    ("h\\e", 0, True, ["h\\e"], 3),
    # 无效转义字符
    ("h\\x", 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert actual_end == expected_end, f"Expected end {expected_end}, got {actual_end}"
    except ValueError as e:
        assert expected_parts is None and expected_end is None, f"Unexpected error: {e}"