# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 2, 迭代: 7
# 生成时间: 2026-04-18 16:42:13

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end, expected_exception", [
    # 正常情况：字符串以双引号结束，无转义
    ("\"hello\"", 1, True, ["hello"], 6, None),
    # 正常情况：字符串包含转义字符
    ("\"hello\\\"world\"", 1, True, ["hello\"world"], 12, None),
    # 转义字符不是双引号的情况
    ("\"hello\\\\world\"", 1, True, ["hello\\world"], 11, None),
    # 转义字符无效
    ("\"hello\\xworld\"", 1, True, None, None, ValueError),
    # 字符串未正确结束
    ("\"hello", 1, True, None, None, ValueError),
    # 空字符串
    ("\"", 1, True, [""], 2, None),
    # 多个转义字符
    ("\"hello\\\\\\\"world\"", 1, True, ["hello\\\\\"world"], 14, None),
    # 边界情况：字符串只有一个字符
    ("\"\"", 1, True, [""], 2, None),
    # 严格模式下，非双引号字符被处理
    ("\"hello\\x\"", 1, True, None, None, ValueError),
    # 非严格模式下，忽略非法转义
    ("\"hello\\x\"", 1, False, ["hello\\x"], 6, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            result = scanstring(s, end, strict)
    else:
        result = scanstring(s, end, strict)
        assert result[0] == ''.join(expected_parts)
        assert result[1] == expected_end