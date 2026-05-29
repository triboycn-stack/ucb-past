# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 4, 迭代: 4
# 生成时间: 2026-05-23 09:23:33

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后无内容
    ('"hello\\\\"', 1, True, ['hello"'], 8),
    # 字符串中包含多个转义
    ('"h\\e\\l\\l\\o"', 1, True, ['helo'], 10),
    # 空字符串（应抛出异常）
    ('"', 1, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"hello', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"this is a very long string with many characters"', 1, True, ['this is a very long string with many characters'], 47),
    # 转义字符后没有内容（错误情况）
    ('"hello\\', 1, True, None, None),
    # 转义字符无效
    ('"hello\\x"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert final_end == expected_end, f"Expected end index {expected_end}, got {final_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected no exception, but got one"