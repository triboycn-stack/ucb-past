# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 3, 迭代: 3
# 生成时间: 2026-04-18 16:43:30

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符处理
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 11),
    # 转义字符错误
    ('"hello\\x"', 1, True, None, None),
    # 空字符串（非法）
    ('""', 1, True, None, None),
    # 未终止字符串（抛出异常）
    ('"hello', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 多个转义字符组合
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 转义后继续处理
    ('"hello\\\"world\\\"test"', 1, True, ['hello"world"test'], 17),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end index {expected_end}, got {new_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected no exception but got one"