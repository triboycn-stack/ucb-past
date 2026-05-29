# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 0, 迭代: 6
# 生成时间: 2026-04-18 16:37:33

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 测试带转义字符的字符串
    ('"hello\\world"', 1, True, ['hello\\world'], 12),
    # 测试转义字符为反斜杠的情况
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 测试转义字符为双引号的情况
    ('"hello\\"world"', 1, True, ['hello"world'], 12),
    # 测试多个转义字符
    ('"hello\\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 测试空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 测试未闭合的字符串（应抛出异常）
    ('"hello', 1, True, None, None),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 测试多轮循环处理
    ('"a\\b\\c\\d"', 1, True, ['a\\b\\c\\d'], 8),
    # 测试转义字符后接其他字符
    ('"a\\b c"', 1, True, ['a\\b c'], 7),
    # 测试转义字符后接换行
    ('"a\\n b"', 1, True, ['a\n b'], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert final_end == expected_end
    except ValueError as e:
        assert expected_parts is None and expected_end is None
        assert str(e) == "Unterminated string"