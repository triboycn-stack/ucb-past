# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 2, 迭代: 13
# 生成时间: 2026-04-18 16:42:54

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符处理
    ('"he\\\"llo"', 1, True, ['he"llo'], 7),
    # 多个转义字符
    ('"he\\\\llo"', 1, True, ['he\\llo'], 7),
    # 转义字符后无内容
    ('"h\\\\"', 1, True, ['h"'], 5),
    # 转义字符错误
    ('"h\\x"', 1, True, None, None),
    # 字符串未闭合（异常）
    ('"h', 1, True, None, None),
    # 空字符串（异常）
    ('"', 0, True, None, None),
    # 多个部分拼接
    ('"ha\\\"llo\\\"world"', 1, True, ['ha"llo"world'], 13),
    # 边界情况：字符串开始于索引0
    ('"test"', 0, True, ['test'], 5),
    # 边界情况：字符串结束于末尾
    ('"end"', 0, True, ['end'], 4),
    # 长字符串
    ('"a" * 100', 1, True, ['a' * 100], 1 + 100 + 1),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end {expected_end}, got {new_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but got no exception"