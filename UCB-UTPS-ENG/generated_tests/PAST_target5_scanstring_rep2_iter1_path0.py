# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 2, 迭代: 1
# 生成时间: 2026-05-23 09:21:00

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常字符串，无转义字符
    ("hello", 0, True, ["hello"], 5),
    # 测试带转义字符的字符串
    ("hello\\world", 0, True, ["hello\\world"], 11),
    # 测试转义字符为反斜杠的情况
    ("hello\\\\world", 0, True, ["hello\\world"], 12),
    # 测试转义字符为双引号的情况
    ("hello\"world", 0, True, ["hello\"world"], 11),
    # 测试多个转义字符
    ("hello\\\\\"world", 0, True, ["hello\\\"world"], 13),
    # 测试空字符串（应抛出异常）
    ("", 0, True, None, None),
    # 测试未闭合的字符串（应抛出异常）
    ("hello", 0, True, None, None),
    # 测试边界情况：单个字符
    ("a", 0, True, ["a"], 1),
    # 测试多转义字符
    ("a\\\\b\\\"c", 0, True, ["a\\b\"c"], 8),
    # 测试转义字符后有其他字符
    ("abc\\def", 0, True, ["abc\\def"], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end