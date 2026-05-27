# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 0, 迭代: 1
# 生成时间: 2026-05-23 09:19:00

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end, expected_exception", [
    # 正常情况：字符串正常结束
    ('"hello"', 1, True, ['hello'], 6, None),
    # 转义字符处理
    ('"hello\\\"world"', 1, True, ['hello"world'], 13, None),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12, None),
    # 转义字符错误
    ('"hello\\xworld"', 1, True, [], 7, ValueError),
    # 字符串未闭合（边界条件）
    ('"hello', 1, True, [], 1, ValueError),
    # 空字符串（边界条件）
    ('""', 1, True, [''], 2, None),
    # 单个字符
    ('"a"', 1, True, ['a'], 2, None),
    # 多个转义字符处理
    ('"a\\nb\\tc\\rd"', 1, True, ['a\nb\tc\rd'], 8, None),
    # 转义字符后无内容
    ('"\\\\"', 1, True, ['\\'], 3, None),
    # 转义字符后无闭合引号
    ('"\\\"', 1, True, [], 2, ValueError),
    # 转义字符后无效
    ('"\\x"', 1, True, [], 2, ValueError),
    # 严格模式下转义字符错误
    ('"\\x"', 1, True, [], 2, ValueError),
    # 非严格模式下允许未知转义
    ('"\\x"', 1, False, ['\\x'], 3, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            result, new_end = scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end