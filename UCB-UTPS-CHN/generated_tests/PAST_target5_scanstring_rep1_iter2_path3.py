# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '"'
# 重复次数: 1, 迭代: 2
# 生成时间: 2026-04-18 16:39:27

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常字符串，包含转义字符
    ('"hello\\"world"', 1, True, ['hello"world'], 12),
    # 测试转义字符为双引号的情况
    ('"hello\\\\\"world"', 1, True, ['hello\\"world'], 13),
    # 测试空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 测试未终止的字符串
    ('"hello', 0, True, None, None),
    # 测试多个转义字符
    ('"hello\\\\\\\"world"', 1, True, ['hello\\\"world'], 14),
    # 测试单个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 11),
    # 测试没有转义字符的字符串
    ('"hello world"', 1, True, ['hello world'], 12),
    # 测试边界情况：字符串长度为1
    ('"a"', 1, True, ['a'], 2),
    # 测试字符串中包含多个转义字符
    ('"hello\\\\\\\"world\\\\\\\"test"', 1, True, ['hello\\\\\"world\\\\\"test'], 20),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, end_index = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert end_index == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None