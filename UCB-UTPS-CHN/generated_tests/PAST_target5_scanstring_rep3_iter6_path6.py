# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 3, 迭代: 6
# 生成时间: 2026-05-23 09:22:48

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 基本情况：正常字符串，以双引号结束
    ('"hello"', 1, True, 'hello', 6),
    # 带转义字符的情况：转义双引号
    ('"hello\\"world"', 1, True, 'hello"world', 13),
    # 带转义字符的情况：转义反斜杠
    ('"hello\\\\world"', 1, True, 'hello\\world', 13),
    # 转义字符错误的情况
    ('"hello\\x"', 1, True, None, None),
    # 字符串未闭合（抛出异常）
    ('"hello', 1, True, None, None),
    # 空字符串（抛出异常）
    ('"', 1, True, None, None),
    # 多个转义字符
    ('"hello\\\\\\"world"', 1, True, 'hello\\"world', 15),
    # 边界情况：单个字符
    ('"a"', 1, True, 'a', 3),
    # 边界情况：空字符串（非法）
    ('', 0, True, None, None),
    # 非法输入：非字符串
    (123, 0, True, None, None),
    # 非法输入：end参数超出范围
    ('"hello"', 10, True, None, None),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == expected_value
        assert new_end == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None