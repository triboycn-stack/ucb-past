# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '"'
# 重复次数: 2, 迭代: 4
# 生成时间: 2026-05-23 09:21:21

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试 esc == '"'
    ('"hello\"world"', 1, True, ['hello"world'], 12),
    # 测试正常字符串结束
    ('"hello world"', 1, True, ['hello world'], 12),
    # 测试转义字符
    ('"hello\\"world"', 1, True, ['hello"world'], 13),
    # 测试多转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 14),
    # 测试空字符串（应抛出异常）
    ('"', 1, True, None, None),
    # 测试未终止字符串
    ('"hello', 1, True, None, None),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 测试带多个转义字符的字符串
    ('"hello\\\\\"world"', 1, True, ['hello\\"world'], 16),
    # 测试包含多个转义和普通字符
    ('"hello\\\"world\\t"', 1, True, ['hello"world\t'], 17),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end {expected_end}, got {new_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but no exception raised"