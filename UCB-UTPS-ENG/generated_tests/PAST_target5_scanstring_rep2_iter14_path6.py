# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 2, 迭代: 14
# 生成时间: 2026-04-18 16:43:02

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 0, True, ['hello'], 6),
    # 带转义字符的字符串
    ('"he\\\"llo"', 0, True, ['he"llo'], 8),
    # 多个转义字符
    ('"he\\\\llo"', 0, True, ['he\\llo'], 8),
    # 转义后直接结束
    ('"he\\"', 0, True, ['he"'], 6),
    # 空字符串（错误）
    ('""', 0, True, [''], 2),
    # 未闭合的字符串（抛出异常）
    pytest.param('"hello', 0, True, None, None, marks=pytest.mark.xfail(raises=ValueError)),
    # 转义错误（非法转义）
    pytest.param('"he\\x"', 0, True, None, None, marks=pytest.mark.xfail(raises=ValueError)),
    # 边界情况：单字符字符串
    ('"a"', 0, True, ['a'], 2),
    # 多次转义
    ('"he\\\\\\\"llo"', 0, True, ['he\\\\"llo'], 10),
    # 字符串中间有换行
    ('"hello\nworld"', 0, True, ['hello\nworld'], 12),
    # 严格模式下，非法字符
    pytest.param('"hello\x00"', 0, True, None, None, marks=pytest.mark.xfail(raises=ValueError)),
    # 非严格模式下，允许非法字符
    ('"hello\x00"', 0, False, ['hello\x00'], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end