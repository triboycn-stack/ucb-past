# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '"'
# 重复次数: 4, 迭代: 3
# 生成时间: 2026-05-23 09:23:26

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试 esc == '"'
    ('"hello\"world"', 1, True, ['hello"world'], 12),
    # 测试正常字符串结束
    ('"hello world"', 1, True, ['hello world'], 12),
    # 测试转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 测试空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 测试未终止字符串
    ('"hello', 1, True, None, None),
    # 测试多转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 测试多个转义字符
    ('"hello\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 测试带前导空格和转义
    ('"  \\\"test\"  "', 1, True, ['  "test'], 8),
    # 测试带多个转义
    ('"a\\\\b\\\"c"', 1, True, ['a\\b"c'], 9),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end {expected_end}, got {new_end}"
    except ValueError as e:
        assert expected_parts is None and expected_end is None, f"Unexpected error: {e}"