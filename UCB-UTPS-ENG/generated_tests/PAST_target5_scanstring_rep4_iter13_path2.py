# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 4, 迭代: 13
# 生成时间: 2026-04-18 16:46:28

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello\"world", 0, True, ["hello"], 5),
    # 转义字符处理
    ("hello\\\"world", 0, True, ["hello\""], 7),
    # 多个转义字符
    ("hello\\\\world", 0, True, ["hello\\"], 7),
    # 转义字符后无结束引号（错误情况）
    ("hello\\", 0, True, None, None),
    # 空字符串（错误情况）
    ("\"", 0, True, None, None),
    # 字符串中间有转义
    ("h\\\"ello\"world", 0, True, ["h\"ello"], 8),
    # 多个转义字符
    ("a\\b\\c\"d", 0, True, ["a\\b\\c"], 6),
    # 边界情况：字符串长度为1
    ("\"", 0, True, None, None),
    # 长字符串
    ("a" * 100 + "\"", 0, True, [ "a" * 100 ], 100),
    # 转义字符后有其他字符
    ("h\\e\"llo", 0, True, ["h"], 2),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end {expected_end}, got {new_end}"
    except ValueError as e:
        assert expected_parts is None and expected_end is None, f"Unexpected error: {e}"