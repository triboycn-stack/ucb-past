# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 4, 迭代: 8
# 生成时间: 2026-04-18 16:45:52

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常字符串，无转义字符
    ('"hello"', 1, True, ['hello'], 6),
    # 测试带转义字符的字符串
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 测试转义字符为反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 测试转义字符为其他字符（触发异常）
    ('"hello\\xworld"', 1, True, None, None),
    # 测试字符串未闭合（触发异常）
    ('"hello', 1, True, None, None),
    # 测试空字符串（触发异常）
    ('"', 1, True, None, None),
    # 测试多段字符串拼接
    ('"hello\\\"world\\\"test"', 1, True, ['hello"world"test'], 15),
    # 测试转义字符后跟其他字符
    ('"hello\\xworld"', 1, True, None, None),
    # 测试转义字符后跟反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end