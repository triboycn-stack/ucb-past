# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 4, 迭代: 11
# 生成时间: 2026-04-18 16:46:13

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("\"hello world\"", 1, True, ["hello world"], 13),
    # 转义字符 " 的情况
    ("\"hello\\\"world\"", 1, True, ["hello\"world"], 14),
    # 转义字符 \ 的情况
    ("\"hello\\\\world\"", 1, True, ["hello\\world"], 14),
    # 转义字符其他情况（触发异常）
    ("\"hello\\xworld\"", 1, True, None, None),
    # 空字符串（错误）
    ("\"", 0, True, None, None),
    # 字符串未闭合（错误）
    ("\"hello", 1, True, None, None),
    # 多个转义字符
    ("\"hello\\\\\\\"world\"", 1, True, ["hello\\\\\"world"], 16),
    # 边界情况：单个字符
    ("\"a\"", 1, True, ["a"], 3),
    # 长字符串
    ("\"abcdefghijklmnopqrstuvwxyz\"", 1, True, ["abcdefghijklmnopqrstuvwxyz"], 27),
    # 包含多个转义字符
    ("\"hello\\\\\\\"world\\t\"", 1, True, ["hello\\\\\"world\t"], 18),
    # 转义字符后无内容（错误）
    ("\"hello\\\"", 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, actual_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert actual_end == expected_end