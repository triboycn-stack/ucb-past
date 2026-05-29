# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '"'
# 重复次数: 2, 迭代: 10
# 生成时间: 2026-04-18 16:42:34

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_value, expected_end", [
    # 测试正常情况：字符串以双引号结束
    ('"hello"', 0, True, 'hello', 6),
    # 测试转义字符：\" 被处理为 "
    ('"hello\\"world"', 0, True, 'hello"world', 13),
    # 测试转义字符：\\ 被处理为 \
    ('"hello\\\\world"', 0, True, 'hello\\world', 13),
    # 测试转义字符：其他非法转义（应抛出异常）
    ('"hello\\xworld"', 0, True, None, None),
    # 测试字符串中包含多个转义字符
    ('"hello\\\"world\\\\test"', 0, True, 'hello"world\\test', 17),
    # 测试空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 测试未终止的字符串（索引越界）
    ('"hello', 0, True, None, None),
    # 测试字符串中间有转义字符
    ('"h\\\"ello"', 0, True, 'h"ello', 8),
    # 测试字符串中有多个转义字符
    ('"h\\\\\\\"ello"', 0, True, 'h\\\\"ello', 11),
    # 测试边界情况：单个字符
    ('"a"', 0, True, 'a', 2),
    # 测试字符串中没有转义字符
    ('"abc123"', 0, True, 'abc123', 7),
    # 测试字符串中包含换行符
    ('"hello\nworld"', 0, True, 'hello\nworld', 12),
    # 测试字符串中包含制表符
    ('"hello\tworld"', 0, True, 'hello\tworld', 12),
])
def test_scanstring(s, end, strict, expected_value, expected_end):
    if expected_value is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        value, new_end = scanstring(s, end, strict)
        assert value == expected_value
        assert new_end == expected_end