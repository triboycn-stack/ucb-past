# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 4, 迭代: 2
# 生成时间: 2026-05-23 09:23:19

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
    # 未终止字符串（抛出异常）
    ('"hello', 1, True, None, None),
    # 边界情况：单字符字符串
    ('"a"', 1, True, ['a'], 3),
    # 多次转义
    ('"hello\\\\\\\"world"', 1, True, ['hello\\\\"world'], 15),
    # 转义后无内容
    ('"\\\""', 1, True, ['"'], 4),
    # 转义后有其他字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义后有多个字符
    ('"hello\\\\world\\\"test"', 1, True, ['hello\\world"test'], 16),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert final_end == expected_end, f"Expected end {expected_end}, got {final_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected no exception, but got one"