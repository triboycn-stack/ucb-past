# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 2, 迭代: 3
# 生成时间: 2026-05-23 09:21:14

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello\"", 0, True, ["hello"], 6),
    # 转义字符：\" -> "
    ("hello\\\"", 0, True, ["hello\""], 7),
    # 转义字符：\\ -> \
    ("hello\\\\world", 0, True, ["hello\\world"], 12),
    # 多个转义字符
    ("hello\\\\\"world", 0, True, ["hello\\\"world"], 13),
    # 空字符串（应抛出异常）
    ("\"", 0, True, None, None),
    # 未终止的字符串（应抛出异常）
    ("hello", 0, True, None, None),
    # 转义字符后无内容（应抛出异常）
    ("hello\\", 0, True, None, None),
    # 边界情况：单个转义字符
    ("\\\"", 0, True, ["\""], 2),
    # 边界情况：多个转义字符
    ("\\\\\"", 0, True, ["\\\""], 3),
    # 转义字符后有其他字符
    ("hello\\a\"", 0, True, None, None),
    # 转义字符后没有有效字符（应抛出异常）
    ("hello\\", 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        parts = []
        current = 0
        while current < len(result):
            if result[current] == '\\':
                parts.append(result[current:current+2])
                current += 2
            else:
                parts.append(result[current])
                current += 1
        assert parts == expected_parts
        assert final_end == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None