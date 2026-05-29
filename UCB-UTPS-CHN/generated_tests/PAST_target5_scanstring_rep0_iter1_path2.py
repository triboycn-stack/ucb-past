# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 0, 迭代: 1
# 生成时间: 2026-04-18 16:36:58

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常字符串，无转义字符
    ("hello", 0, True, ["hello"], 5),
    # 测试带转义字符的字符串
    ('"hello\\\"world"', 1, True, ["hello\"world"], 13),
    # 测试转义字符为反斜杠
    ('"hello\\\\world"', 1, True, ["hello\\world"], 12),
    # 测试转义字符为其他字符（触发异常）
    ('"hello\\xworld"', 1, True, None, None),
    # 测试字符串未闭合（触发异常）
    ('"hello', 0, True, None, None),
    # 测试空字符串（触发异常）
    ('"', 0, True, None, None),
    # 测试多段字符串（包含转义）
    ('"hello\\\"world\\\"test"', 1, True, ["hello\"world\"test"], 17),
    # 测试转义后继续处理
    ('"a\\nb\\tc\\td"', 1, True, ["a\nb\tc\td"], 9),
    # 测试边界情况：字符串长度为1
    ('"', 0, True, None, None),
    # 测试字符串中包含多个转义
    ('"a\\\\b\\\\c"', 1, True, ["a\\b\\c"], 8),
    # 测试严格模式下非法转义
    ('"a\\x"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end