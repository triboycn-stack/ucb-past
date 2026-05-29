# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 1, 迭代: 1
# 生成时间: 2026-04-18 16:39:21

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符处理
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后无内容
    ('"hello\\"', 1, True, ['hello"'], 7),
    # 转义字符错误
    ('"hello\\x"', 1, True, None, None),
    # 空字符串（非法）
    ('""', 1, True, None, None),
    # 字符串未闭合（非法）
    ('"hello', 1, True, None, None),
    # 多次循环处理
    ('"a\\nb\\nc"', 1, True, ['a\nb\nc'], 8),
    # 边界情况：单字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"this is a long string with many characters and some \\\"quotes\\\"."', 1, True, ['this is a long string with many characters and some "quotes"."'], 49),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert final_end == expected_end, f"Expected end index {expected_end}, got {final_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected no exception but got one"