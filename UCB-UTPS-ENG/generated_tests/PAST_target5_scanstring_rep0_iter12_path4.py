# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 0, 迭代: 12
# 生成时间: 2026-04-18 16:38:14

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello", 0, True, ["hello"], 5),
    # 带有转义字符的情况
    ('hello\\"world', 0, True, ["hello\"world"], 12),
    # 转义字符后接其他字符（如 \\）
    ('hello\\\\world', 0, True, ["hello\\world"], 12),
    # 转义字符后接非法字符（应抛出异常）
    ('hello\\xworld', 0, True, None, None),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 字符串中包含多个转义
    ('a\\nb\\tc\\rd', 0, True, ["a\nb\tc\rd"], 8),
    # 边界情况：字符串开始于转义字符
    ('\\abc', 0, True, ["\\abc"], 4),
    # 多个转义字符连续
    ('\\\\\\', 0, True, ["\\\\\\"], 4),
    # 长字符串
    ('a' * 100, 0, True, [f"a"*100], 100),
    # 未终止的字符串（应抛出异常）
    ('hello', 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, actual_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert actual_end == expected_end