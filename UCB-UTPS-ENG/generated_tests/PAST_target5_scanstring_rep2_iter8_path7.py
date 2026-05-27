# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '"')
# 重复次数: 2, 迭代: 8
# 生成时间: 2026-05-23 09:21:53

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义字符
    ("hello\"", 0, True, ["hello"], 6),
    # 带转义字符的情况
    ("hello\\\"world\"", 0, True, ["hello\"world"], 13),
    # 多个转义字符
    ("hello\\\\world\"", 0, True, ["hello\\world"], 14),
    # 转义字符后没有闭合引号（应抛出异常）
    ("hello\\", 0, True, None, None),
    # 字符串中包含换行符
    ("hello\nworld\"", 0, True, ["hello\nworld"], 12),
    # 空字符串（应抛出异常）
    ("\"", 0, True, None, None),
    # 转义字符无效
    ("hello\\x\"", 0, True, None, None),
    # 多次转义
    ("hello\\\\\\\"world\"", 0, True, ["hello\\\\\"world"], 16),
    # 边界情况：字符串开始于引号
    ("\"hello\"", 0, True, ["hello"], 7),
    # 引号在中间
    ("abc\"def\"", 0, True, ["abc", "def"], 8),
    # 长字符串
    ("a" * 100 + "\"", 0, True, ["a" * 100], 101),
    # 转义字符在末尾
    ("hello\\\"", 0, True, ["hello\""], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end