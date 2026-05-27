# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 0, 迭代: 7
# 生成时间: 2026-04-18 16:37:39

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符：\" 
    ('"he\\\"llo"', 1, True, ['he"llo'], 7),
    # 转义字符：\\
    ('"he\\\\llo"', 1, True, ['he\\llo'], 7),
    # 转义字符：其他（触发异常）
    ('"he\\x llo"', 1, True, None, None),
    # 未终止字符串（触发异常）
    ('"hello', 1, True, None, None),
    # 空字符串（触发异常）
    ('"', 1, True, None, None),
    # 多个转义字符
    ('"he\\\"llo\\\\world"', 1, True, ['he"llo\\world'], 13),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 边界情况：空字符串（错误）
    ('"', 0, True, None, None),
    # 边界情况：长字符串
    ('"a" * 100', 1, True, ['a' * 100], 101),
    # 无效转义字符（触发异常）
    ('"he\\z llo"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end