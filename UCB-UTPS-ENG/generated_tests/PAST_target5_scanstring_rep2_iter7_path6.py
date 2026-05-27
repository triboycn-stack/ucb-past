# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 2, 迭代: 7
# 生成时间: 2026-05-23 09:21:45

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 正常情况：字符串以双引号结束
    ("\"hello\"", 1, True, "hello", 6),
    # 转义字符处理：转义双引号
    ("\"hello\\\"world\"", 1, True, "hello\"world", 13),
    # 转义字符处理：转义反斜杠
    ("\"hello\\\\world\"", 1, True, "hello\\world", 12),
    # 多个转义字符
    ("\"hello\\\\\\\"world\"", 1, True, "hello\\\"world", 14),
    # 字符串中间有普通字符
    ("\"abc123\"", 1, True, "abc123", 7),
    # 空字符串（非法，但根据逻辑会抛出异常）
    ("\"", 0, True, None, None),
    # 未终止字符串（抛出异常）
    ("\"hello", 1, True, None, None),
    # 边界情况：字符串长度为1
    ("\"\"", 1, True, "", 2),
    # 转义字符在字符串末尾
    ("\"hello\\\\\"", 1, True, "hello\\", 8),
    # 多次循环处理
    ("\"a\\nb\\tc\"", 1, True, "a\nb\tc", 9),
    # 异常处理：无效转义字符
    ("\"hello\\xworld\"", 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    if expected_value is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result_value, result_end = scanstring(s, end, strict)
        assert result_value == expected_value
        assert result_end == expected_end