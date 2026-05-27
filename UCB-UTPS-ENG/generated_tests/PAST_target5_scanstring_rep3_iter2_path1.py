# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 3, 迭代: 2
# 生成时间: 2026-04-18 16:43:24

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串被双引号结束
    ('"hello"', 0, True, ['hello'], 6),
    # 转义字符处理：\"
    ('"hello\\"world"', 0, True, ['hello"world'], 12),
    # 转义字符处理：\\
    ('"hello\\\\world"', 0, True, ['hello\\world'], 12),
    # 转义字符处理：其他非法转义
    ('"hello\\xworld"', 0, True, None, None),  # 应该抛出异常
    # 空字符串（非法）
    ('""', 0, True, [''], 2),
    # 字符串中间有转义
    ('"h\\ne\\twor\\ld"', 0, True, ['h\ne\tworld'], 13),
    # 边界情况：字符串长度为1
    ('"a"', 0, True, ['a'], 2),
    # 多个转义字符
    ('"a\\\\b\\\"c"', 0, True, ['a\\b"c'], 9),
    # 未终止的字符串（抛出异常）
    ('"unterminated', 0, True, None, None),
    # 严格模式下非法转义
    ('"invalid\\x"', 0, True, None, None),
    # 非严格模式下允许非法转义
    ('"invalid\\x"', 0, False, ['invalid\\x'], 8),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end