# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 4, 迭代: 14
# 生成时间: 2026-04-18 16:46:39

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 正常情况：字符串被正确解析
    ('"hello"', 1, True, 'hello', 6),
    # 转义字符处理：\"
    ('"hello\\"world"', 1, True, 'hello"world', 12),
    # 转义字符处理：\\
    ('"hello\\\\world"', 1, True, 'hello\\world', 12),
    # 转义字符处理：其他字符（触发异常）
    ('"hello\\xworld"', 1, True, None, None),
    # 未终止的字符串（抛出异常）
    ('"hello', 1, True, None, None),
    # 空字符串（抛出异常）
    ('""', 1, True, None, None),
    # 多个转义字符
    ('"hello\\\\\\"world"', 1, True, 'hello\\"world', 14),
    # 边界情况：单个字符
    ('"a"', 1, True, 'a', 3),
    # 边界情况：空字符串（无引号）
    ('', 0, True, None, None),
    # 非字符串输入（抛出异常）
    (123, 0, True, None, None),
    # 非字符串输入（抛出异常）
    (None, 0, True, None, None),
    # 无效的end参数（抛出异常）
    ('"hello"', -1, True, None, None),
    # 无效的end参数（超出范围）
    ('"hello"', 100, True, None, None),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    if expected_value is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, result_end = scanstring(s, end, strict)
        assert result == expected_value
        assert result_end == expected_end