# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 1, 迭代: 13
# 生成时间: 2026-04-18 16:40:51

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end, expected_exception", [
    # 正常情况：字符串正常结束
    ('"hello"', 1, True, ['hello'], 6, None),
    # 转义字符处理
    ('"hello\\\"world"', 1, True, ['hello"world'], 13, None),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12, None),
    # 转义字符错误
    ('"hello\\x"', 1, True, [], 6, ValueError),
    # 字符串未闭合
    ('"hello', 1, True, [], 1, ValueError),
    # 空字符串
    ('""', 1, True, [''], 2, None),
    # 带有换行符的字符串
    ('"hello\nworld"', 1, True, ['hello\nworld'], 12, None),
    # 带有多个转义字符的字符串
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 14, None),
    # 边界情况：字符串长度为1
    ('"', 0, True, [], 0, ValueError),
    # 无效转义字符
    ('"hello\\z"', 1, True, [], 6, ValueError),
    # 严格模式下，非转义字符处理
    ('"hello world"', 1, True, ['hello world'], 11, None),
    # 非严格模式下，允许某些特殊字符
    ('"hello\\x"', 1, False, ['hello\\x'], 6, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            result = scanstring(s, end, strict)
    else:
        result = scanstring(s, end, strict)
        assert isinstance(result, tuple), "返回值应为元组"
        value, next_end = result
        assert value == ''.join(expected_parts), f"期望的字符串部分为 {expected_parts}, 实际为 {value}"
        assert next_end == expected_end, f"期望的下一个索引为 {expected_end}, 实际为 {next_end}"