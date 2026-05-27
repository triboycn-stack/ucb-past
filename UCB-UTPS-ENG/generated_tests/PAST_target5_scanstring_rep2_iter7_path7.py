# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 2, 迭代: 7
# 生成时间: 2026-05-23 09:16:25

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ("hello\"world", 0, True, ["hello"], 5),
    # 转义字符处理：双引号转义
    ("hello\\\"world", 0, True, ["hello\""], 6),
    # 转义字符处理：反斜杠转义
    ("hello\\\\world", 0, True, ["hello\\"], 6),
    # 多个转义字符
    ("hello\\\\\"world", 0, True, ["hello\\\""], 7),
    # 空字符串（应抛出异常）
    ("", 0, True, None, None),
    # 字符串未闭合（应抛出异常）
    ("hello", 0, True, None, None),
    # 包含换行符的字符串
    ("hello\nworld", 0, True, ["hello\n"], 5),
    # 多次循环处理
    ("h\\\"e\\\"l\\\"o\"", 0, True, ["h\"e\"l\"o"], 8),
    # 边界情况：单个字符
    ("a\"", 0, True, ["a"], 1),
    # 非法转义字符
    ("hello\\xworld", 0, True, None, None),
    # 严格模式下非法转义字符
    ("hello\\xworld", 0, True, None, None),
    # 非严格模式下允许非法转义字符
    ("hello\\xworld", 0, False, ["hello\\x"], 6),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end