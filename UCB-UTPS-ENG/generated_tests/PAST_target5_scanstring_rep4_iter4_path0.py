# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 4, 迭代: 4
# 生成时间: 2026-04-18 16:45:20

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常情况：无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 测试转义字符：\"
    ('"hello\\"world"', 1, True, ['hello"world'], 12),
    # 测试转义字符：\\
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 测试转义字符：其他（应抛出异常）
    ('"hello\\xworld"', 1, True, None, None),
    # 测试字符串未闭合（应抛出异常）
    ('"hello', 1, True, None, None),
    # 测试空字符串（应抛出异常）
    ('""', 1, True, None, None),
    # 测试多转义字符
    ('"hello\\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 测试长字符串
    ('"abcdefghijklmnopqrstuvwxyz"', 1, True, ['abcdefghijklmnopqrstuvwxyz'], 27),
    # 测试转义后继续处理
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 测试转义后有其他字符
    ('"hello\\\\world\\n"', 1, True, ['hello\\world\n'], 13),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end