# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 1, 迭代: 9
# 生成时间: 2026-04-18 16:40:20

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串被正确解析
    ("\"hello\"", 1, True, ["hello"], 7),
    # 转义字符处理：\" 被转换为 "
    ("\"hello\\\"world\"", 1, True, ["hello\"world"], 14),
    # 多个转义字符处理：\\ 被转换为 \
    ("\"hello\\\\world\"", 1, True, ["hello\\world"], 14),
    # 转义字符处理：其他转义字符（如 \n）抛出异常
    ("\"hello\\nworld\"", 1, True, None, None),
    # 未终止的字符串
    ("\"hello", 1, True, None, None),
    # 空字符串
    ("\"", 1, True, [""], 2),
    # 带有多个转义字符的字符串
    ("\"hello\\\\\\\"world\"", 1, True, ["hello\\\"world"], 16),
    # 边界情况：字符串开始于索引0
    ("\"test\"", 0, True, ["test"], 6),
    # 边界情况：字符串结束于索引末尾
    ("\"end\"", 1, True, ["end"], 5),
    # 异常情况：转义字符后没有字符
    ("\"hello\\\"", 1, True, None, None),
    # 异常情况：转义字符无效
    ("\"hello\\x\"", 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, actual_end = scanstring(s, end, strict)
        assert expected_parts is not None
        assert expected_parts == result.split('\n') if '\n' in result else [result]
        assert actual_end == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None