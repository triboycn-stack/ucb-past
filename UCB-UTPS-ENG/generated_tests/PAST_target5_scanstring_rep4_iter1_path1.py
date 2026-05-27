# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 4, 迭代: 1
# 生成时间: 2026-05-23 09:23:11

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串以双引号结束，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符处理：\" -> "
    ('"he\\\"llo"', 1, True, ['he"llo'], 8),
    # 转义字符处理：\\ -> \
    ('"he\\\\llo"', 1, True, ['he\\llo'], 8),
    # 转义字符处理：其他非法转义
    ('"he\\x",', 1, True, None, None),
    # 字符串未闭合（抛出异常）
    ('"hello', 1, True, None, None),
    # 空字符串（抛出异常）
    ('""', 1, True, None, None),
    # 多个转义字符
    ('"he\\\"llo\\\\world"', 1, True, ['he"llo\\world'], 14),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 边界情况：字符串中间有换行
    ('"hello\nworld"', 1, True, ['hello\nworld'], 12),
    # 转义字符后没有内容（抛出异常）
    ('"he\\', 1, True, None, None),
    # 严格模式下非法转义
    ('"he\\x"', 1, True, None, None),
    # 非严格模式下允许非法转义
    ('"he\\x"', 1, False, ['he\\x'], 6),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end