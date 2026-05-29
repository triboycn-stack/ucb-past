# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 1, 迭代: 10
# 生成时间: 2026-04-18 16:40:28

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串包含普通字符和转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 转义字符处理
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 多个转义字符
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 13),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 未终止字符串（索引越界）
    ('"hello', 1, True, None, None),
    # 字符串中包含多个非转义字符
    ('"abcde"', 1, True, ['abcde'], 6),
    # 字符串中包含多个转义字符
    ('"a\\\\b\\\"c"', 1, True, ['a\\b"c'], 8),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 边界情况：空字符串（不合法）
    ('""', 0, True, None, None),
    # 严格模式下非法转义
    ('"hello\\x"', 1, True, None, None),
    # 非严格模式下允许非法转义
    ('"hello\\x"', 1, False, ['hello\\x'], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end