# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 3, 迭代: 5
# 生成时间: 2026-05-23 09:22:42

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello\"world", 0, True, ["hello"], 5),
    # 转义字符 " 的情况
    ("hello\"world", 0, True, ["hello", "world"], 11),
    # 转义字符 \ 的情况
    ("hello\\world", 0, True, ["hello\\world"], 11),
    # 转义字符其他情况（触发异常）
    ("hello\\xworld", 0, True, None, None),
    # 空字符串
    ("\"", 0, True, [""], 1),
    # 多个转义字符
    ("hello\\\"world\\\"test", 0, True, ["hello\"", "world\"", "test"], 17),
    # 未终止的字符串（触发异常）
    ("hello", 0, True, None, None),
    # 边界情况：字符串开始于引号
    ("\"world", 0, True, ["world"], 6),
    # 字符串中间有多个转义
    ("a\\\"b\\\"c", 0, True, ["a\"", "b\"", "c"], 9),
    # 严格模式下非法转义
    ("hello\\xworld", 0, True, None, None),
    # 非严格模式下允许非法转义
    ("hello\\xworld", 0, False, ["hello\\xworld"], 10),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end