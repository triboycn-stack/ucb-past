# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 2, 迭代: 6
# 生成时间: 2026-05-23 09:21:37

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串包含转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 正常情况：字符串无转义字符
    ('"hello world"', 1, True, ['hello world'], 12),
    # 转义字符不是 " 的情况
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 多个转义字符
    ('"hello\\\\\\\"world"', 1, True, ['hello\\\\"world'], 15),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 字符串未闭合（应抛出异常）
    ('"hello', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 转义字符后无内容
    ('"\\\\"', 1, True, ['"'], 4),
    # 转义字符后有其他字符
    ('"\\x"', 1, True, ['x'], 4),
    # 多次循环处理
    ('"h\\\"e\\\"l\\\"o"', 1, True, ['h"e"l"o'], 11),
    # 严格模式下非法转义
    ('"h\\x"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end