# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 1, 迭代: 5
# 生成时间: 2026-05-23 09:20:27

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("\"hello world\"", 1, True, ["hello world"], 13),
    # 转义字符 " 的情况
    ("\"hello\\\"world\"", 1, True, ["hello\"world"], 14),
    # 转义字符 \ 的情况
    ("\"hello\\\\world\"", 1, True, ["hello\\world"], 14),
    # 多个转义字符
    ("\"hello\\\\\\\"world\"", 1, True, ["hello\\\\\"world"], 15),
    # 空字符串（应抛出异常）
    ("\"", 1, True, None, None),
    # 转义字符无效
    ("\"hello\\xworld\"", 1, True, None, None),
    # 字符串中包含换行符
    ("\"hello\nworld\"", 1, True, ["hello\nworld"], 13),
    # 边界情况：单字符字符串
    ("\"a\"", 1, True, ["a"], 3),
    # 边界情况：空字符串（未闭合）
    ("\"abc", 1, True, None, None),
    # 多次转义处理
    ("\"hello\\\\\\\"world\"", 1, True, ["hello\\\\\"world"], 16),
    # 转义后未闭合
    ("\"hello\\\"", 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert final_end == expected_end, f"Expected end {expected_end}, got {final_end}"
    except ValueError as e:
        if expected_parts is not None:
            pytest.fail(f"Unexpected exception: {e}")