# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 3, 迭代: 8
# 生成时间: 2026-04-18 16:44:02

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello", 0, True, ["hello"], 5),
    # 转义字符处理
    ('hello\\"world', 0, True, ["hello\"world"], 12),
    # 多个转义字符
    ('hello\\\\world', 0, True, ["hello\\world"], 12),
    # 转义字符后无结束引号（异常）
    ('hello\\', 0, True, None, None),
    # 空字符串（异常）
    ('"', 0, True, None, None),
    # 字符串中包含多个转义
    ('a\\b\\"c', 0, True, ["a\\b\"c"], 7),
    # 边界情况：字符串开始于转义
    ('\\a', 0, True, ["\\a"], 2),
    # 转义后无有效字符（异常）
    ('\\', 0, True, None, None),
    # 长字符串
    ('a' * 100, 0, True, [f"a"*100], 100),
    # 转义字符后有其他字符
    ('abc\\def', 0, True, ["abc\\def"], 7),
    # 转义字符后没有内容（异常）
    ('\\', 0, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert final_end == expected_end, f"Expected end {expected_end}, got {final_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but no exception was raised"