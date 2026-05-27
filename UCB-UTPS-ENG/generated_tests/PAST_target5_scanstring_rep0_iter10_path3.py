# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '"'
# 重复次数: 0, 迭代: 10
# 生成时间: 2026-04-18 16:38:00

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
    # 测试未终止字符串（应抛出异常）
    ('"hello', 1, True, None, None),
    # 测试多转义字符
    ('"hello\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 测试带换行符的字符串
    ('"hello\nworld"', 1, True, ['hello\nworld'], 12),
    # 测试带多个转义字符
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 15),
    # 测试带其他转义字符（触发异常）
    ('"hello\\xworld"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end