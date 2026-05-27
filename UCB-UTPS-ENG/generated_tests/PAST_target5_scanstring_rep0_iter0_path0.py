# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 0, 迭代: 0
# 生成时间: 2026-05-23 09:18:52

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello", 0, True, ["hello"], 5),
    # 转义字符 \"
    ("hello\"world", 0, True, ["hello\"world"], 12),
    # 转义字符 \\
    ("hello\\world", 0, True, ["hello\\world"], 11),
    # 多个转义字符
    ("hello\\\"world", 0, True, ["hello\\\"world"], 12),
    # 空字符串（应抛出异常）
    ("", 0, True, None, None),
    # 未终止的字符串（缺少结尾引号）
    ("hello", 0, True, None, None),
    # 转义字符后没有内容
    ("hello\\", 0, True, None, None),
    # 转义字符无效
    ("hello\\x", 0, True, None, None),
    # 边界情况：单个字符
    ("a", 0, True, ["a"], 1),
    # 长字符串
    ("a" * 100, 0, True, [f"a"*100], 100),
    # 转义字符在中间
    ("h\\e\\l\\l\\o", 0, True, ["h\\e\\l\\l\\o"], 9),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert final_end == expected_end, f"Expected end index {expected_end}, got {final_end}"
    except ValueError:
        assert expected_parts is None and expected_end is None, "Expected exception but got result"