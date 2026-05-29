# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 3, 迭代: 13
# 生成时间: 2026-04-18 16:44:39

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ("hello\"", 0, True, ["hello"], 6),
    # 转义字符 \" 的情况
    ("hello\\\"world\"", 0, True, ["hello\"world"], 13),
    # 转义字符 \\ 的情况
    ("hello\\\\world\"", 0, True, ["hello\\world"], 13),
    # 多个转义字符
    ("hello\\\\\\\"world\"", 0, True, ["hello\\\"world"], 15),
    # 空字符串（应抛出异常）
    ("\"", 0, True, None, None),
    # 未终止的字符串（应抛出异常）
    ("hello", 0, True, None, None),
    # 边界情况：单个字符
    ("\"", 0, True, None, None),
    # 多次循环处理
    ("a\\\"b\\\\c\"", 0, True, ["a\"b\\c"], 11),
    # 严格模式下非法转义
    ("hello\\x\"", 0, True, None, None),
    # 非严格模式下允许非法转义
    ("hello\\x\"", 0, False, ["hellox"], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end