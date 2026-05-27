# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 2, 迭代: 1
# 生成时间: 2026-04-18 16:41:33

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ("hello", 0, True, "hello", 5),
    # 带转义字符的情况
    ("hello\\\"world", 0, True, "hello\"world", 12),
    # 转义字符错误
    ("hello\\xworld", 0, True, None, None),
    # 空字符串（非法）
    ("", 0, True, None, None),
    # 字符串未闭合（非法）
    ("hello", 0, True, None, None),
    # 多个转义字符
    ("hello\\\\\"world", 0, True, "hello\\\"world", 14),
    # 边界情况：字符串长度为1
    ('"', 0, True, "", 1),
    # 转义后继续处理
    ("a\\b\"c", 0, True, "a\\b\"c", 6),
    # 转义后抛出异常
    ("a\\x", 0, True, None, None),
    # 长字符串
    ("a" * 100 + '"', 0, True, "a" * 100, 101),
    # 混合普通字符和转义
    ("abc\\ndef\"ghi", 0, True, "abc\ndef\"ghi", 12),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == expected_value
        assert new_end == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None