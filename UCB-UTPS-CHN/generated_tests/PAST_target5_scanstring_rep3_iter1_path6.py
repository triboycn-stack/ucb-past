# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 3, 迭代: 1
# 生成时间: 2026-04-18 16:43:17

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 基本情况：正常字符串，以双引号结束
    ("hello\"", 0, True, "hello", 6),
    # 转义字符：转义双引号
    ("hello\"world", 0, True, "hello\"world", 12),
    # 转义字符：转义反斜杠
    ("hello\\world", 0, True, "hello\\world", 11),
    # 多个转义字符
    ("hello\"\\world", 0, True, "hello\"\\world", 13),
    # 空字符串（非法）
    ("", 0, True, None, 0),
    # 未闭合的字符串（抛出异常）
    ("hello", 0, True, None, 0),
    # 包含换行符的字符串
    ("hello\nworld\"", 0, True, "hello\nworld", 13),
    # 多个转义字符和普通字符混合
    ("a\\b\"c", 0, True, "a\\b\"c", 7),
    # 边界情况：字符串长度为1
    ("\"", 0, True, "", 1),
    # 边界情况：字符串长度为2（包含转义）
    ("\\\"", 0, True, "\\", 2),
    # 非法转义字符（抛出异常）
    ("hello\\x", 0, True, None, 0),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    if expected_value is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == expected_value
        assert new_end == expected_end