# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 3, 迭代: 7
# 生成时间: 2026-04-18 16:43:55

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 正常情况：字符串以双引号结束
    ('"hello"', 0, True, 'hello', 6),
    # 转义字符处理：转义双引号
    ('"hello\\"world"', 0, True, 'hello"world', 13),
    # 转义字符处理：转义反斜杠
    ('"hello\\\\world"', 0, True, 'hello\\world', 13),
    # 多个转义字符
    ('"hello\\\\\\"world"', 0, True, 'hello\\"world', 14),
    # 未终止的字符串（触发异常）
    ('"hello', 0, True, None, None),
    # 空字符串（触发异常）
    ('"', 0, True, None, None),
    # 边界情况：单个字符
    ('"a"', 0, True, 'a', 2),
    # 转义字符不在允许范围内（触发异常）
    ('"hello\\xworld"', 0, True, None, None),
    # 非严格模式下，忽略非法转义
    ('"hello\\xworld"', 0, False, 'helloxworld', 11),
    # 多次循环处理
    ('"hello\\\"world\\\"test"', 0, True, 'hello"world"test', 17),
    # 空字符串（非严格模式）
    ('"', 0, False, '', 1),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    try:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end
    except ValueError as e:
        assert expected_value is None and expected_end is None
        assert str(e) == "Unterminated string" or str(e) == "Invalid escape"