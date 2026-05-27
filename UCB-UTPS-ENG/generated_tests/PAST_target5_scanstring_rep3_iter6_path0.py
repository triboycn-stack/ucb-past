# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 3, 迭代: 6
# 生成时间: 2026-04-18 16:43:49

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试转义字符 \\ 的情况
    ('hello\\world', 0, True, ['hello\\world'], 11),
    # 测试转义字符 \", 但严格模式下不处理
    ('hello\\"world', 0, True, ['hello\\"world'], 11),
    # 测试转义字符 \", 非严格模式下处理
    ('hello\\"world', 0, False, ['hello"world'], 11),
    # 测试多个转义字符
    ('hello\\\\world', 0, True, ['hello\\\\world'], 12),
    # 测试转义字符后有其他字符
    ('hello\\xworld', 0, True, ['hello\\xworld'], 11),
    # 测试空字符串（应抛出异常）
    ('', 0, True, None, None),
    # 测试未闭合的字符串（应抛出异常）
    ('hello', 0, True, None, None),
    # 测试正常字符串
    ('"hello world"', 1, True, ['hello world'], 12),
    # 测试带转义字符的字符串
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end