# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 0, 迭代: 14
# 生成时间: 2026-04-18 16:39:05

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello", 0, True, "hello", 5),
    # 带转义字符的情况：\\
    ("hello\\\\world", 0, True, "hello\\world", 11),
    # 转义字符后接其他字符（模拟 esc == '\\' 的情况）
    ("hello\\\\world", 0, True, "hello\\world", 11),
    # 转义字符后接双引号
    ("hello\\"world", 0, True, "hello\"world", 9),
    # 空字符串（应抛出异常）
    ("", 0, True, None, None),
    # 字符串未闭合（应抛出异常）
    ("hello", 0, True, None, None),
    # 多个转义字符
    ("h\\e\\l\\l\\o", 0, True, "h\\e\\l\\l\\o", 9),
    # 转义字符后接其他字符（模拟 esc != '\\' 和 esc != '"' 的情况）
    ("h\\e", 0, True, "h\\e", 4),
    # 边界情况：字符串长度为1
    ("\"", 0, True, "\"", 1),
    # 长字符串
    ("a" * 100 + "\"", 0, True, "a" * 100, 101),
    # 转义字符在字符串中间
    ("h\\e\\l\\l\\o", 0, True, "h\\e\\l\\l\\o", 9),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError as e:
        assert expected_value is None and expected_end is None
        assert str(e) == "Unterminated string" or str(e) == "Invalid escape"