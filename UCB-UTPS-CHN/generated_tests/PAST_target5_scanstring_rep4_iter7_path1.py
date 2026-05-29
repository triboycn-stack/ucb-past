# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 4, 迭代: 7
# 生成时间: 2026-04-18 16:45:46

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
    ('"hello\\x"', 1, True, [], 5, ValueError),
    # 字符串未闭合
    ('"hello', 1, True, [], 1, ValueError),
    # 空字符串
    ('""', 1, True, [''], 2, None),
    # 带有换行符的字符串
    ('"hello\nworld"', 1, True, ['hello\nworld'], 12, None),
    # 带有多个转义字符的字符串
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 14, None),
    # 严格模式下转义字符错误
    ('"hello\\x"', 1, True, [], 5, ValueError),
    # 非严格模式下允许未知转义字符
    ('"hello\\x"', 1, False, ['hello\\x'], 5, None),
    # 边界情况：字符串长度为1
    ('"', 0, True, [], 1, ValueError),
    # 边界情况：字符串长度为2（仅引号）
    ('" "', 1, True, [' '], 3, None),
    # 多次循环处理
    ('"a\\nb\\nc"', 1, True, ['a\nb\nc'], 7, None),
    # 转义字符后无内容
    ('"\\\\"', 1, True, ['\\'], 4, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end