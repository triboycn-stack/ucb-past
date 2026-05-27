# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 3, 迭代: 1
# 生成时间: 2026-05-23 09:22:08

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 正常情况：字符串以双引号结束
    ('"hello"', 1, True, 'hello', 6),
    # 转义字符处理：转义双引号
    ('"hello\\"world"', 1, True, 'hello"world', 12),
    # 转义字符处理：转义反斜杠
    ('"hello\\\\world"', 1, True, 'hello\\world', 13),
    # 转义字符处理：无效转义（触发异常）
    ('"hello\\x"', 1, True, None, None),
    # 未终止字符串（触发异常）
    ('"hello', 1, True, None, None),
    # 空字符串（触发异常）
    ('"', 1, True, None, None),
    # 多个转义字符
    ('"hello\\"world\\\\test"', 1, True, 'hello"world\\test', 17),
    # 边界情况：单个字符
    ('"a"', 1, True, 'a', 3),
    # 边界情况：空字符串（无引号）
    ('', 0, True, None, None),
    # 非严格模式下，忽略非法转义
    ('"hello\\x"', 1, False, 'hello\\x', 7),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError:
        assert expected_value is None and expected_end is None