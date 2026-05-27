# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 1, 迭代: 0
# 生成时间: 2026-05-23 09:19:50

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 测试带转义的字符串
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 测试转义字符为反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 测试转义字符为其他字符（触发异常）
    ('"hello\\xworld"', 1, True, None, None),
    # 测试未终止的字符串（抛出异常）
    ('"hello', 1, True, None, None),
    # 测试空字符串（抛出异常）
    ('"', 1, True, None, None),
    # 测试多段字符串
    ('"hello\\\"world\\\"test"', 1, True, ['hello"world"test'], 17),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 测试转义后继续处理
    ('"a\\nb"', 1, True, ['a\nb'], 5),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end