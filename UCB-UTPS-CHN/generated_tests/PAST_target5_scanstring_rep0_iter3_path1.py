# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 0, 迭代: 3
# 生成时间: 2026-04-18 16:37:11

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串被正确解析
    ('"hello"', 0, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 0, True, ['hello"world'], 13),
    # 多个转义字符
    ('"hello\\\\world"', 0, True, ['hello\\world'], 13),
    # 转义字符后无内容
    ('"hello\\"', 0, True, ['hello"'], 7),
    # 字符串中包含多个转义
    ('"hello\\\\\\\"world"', 0, True, ['hello\\"world'], 15),
    # 空字符串（应抛出异常）
    ('""', 0, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"hello', 0, True, None, None),
    # 转义字符后没有字符（应抛出异常）
    ('"hello\\', 0, True, None, None),
    # 非转义字符处理
    ('"abc123"', 0, True, ['abc123'], 7),
    # 边界情况：字符串长度为1
    ('"a"', 0, True, ['a'], 3),
    # 转义字符错误
    ('"hello\\x"', 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end