# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 2, 迭代: 11
# 生成时间: 2026-04-18 16:42:41

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
    ('"hello\\x"', 0, True, None, None),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 字符串未闭合（应抛出异常）
    ('"hello', 0, True, None, None),
    # 多个转义字符
    ('"a\\\"b\\\\c"', 0, True, ['a"b\\c'], 9),
    # 边界情况：单个字符
    ('"a"', 0, True, ['a'], 2),
    # 边界情况：空字符串（无内容）
    ('""', 0, True, [''], 2),
    # 多次循环处理
    ('"abc\\ndef"', 0, True, ['abc\ndef'], 8),
    # 严格模式下非法转义
    ('"hello\\x"', 0, True, None, None),
    # 非严格模式下允许非法转义
    ('"hello\\x"', 0, False, ['hello\\x'], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end