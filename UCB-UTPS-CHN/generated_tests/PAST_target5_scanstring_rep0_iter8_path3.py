# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '"'
# 重复次数: 0, 迭代: 8
# 生成时间: 2026-04-18 16:37:46

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常情况：字符串中包含转义字符 \" 
    ('"hello\"world"', 1, True, ['hello"world'], 12),
    # 测试转义字符 \" 的情况
    ('"hello\\"world"', 1, True, ['hello"world'], 13),
    # 测试空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 测试未终止的字符串（应抛出异常）
    ('"hello', 0, True, None, None),
    # 测试多个转义字符
    ('"hello\\"world\\n"', 1, True, ['hello"world\n'], 15),
    # 测试转义字符后没有内容
    ('"\\', 1, True, None, None),
    # 测试转义字符后有其他字符
    ('"\\a"', 1, True, None, None),
    # 测试转义字符后是双引号
    ('"\\\""', 1, True, ['"'], 4),
    # 测试转义字符后是反斜杠
    ('"\\\\."', 1, True, ['\\'], 5),
    # 测试多段字符串拼接
    ('"hello\\"world\\"test"', 1, True, ['hello"world"test'], 17),
    # 测试边界情况：字符串长度为1
    ('"a"', 1, True, ['a'], 2),
    # 测试字符串中间有转义
    ('"h\\\"ello"', 1, True, ['h"ello'], 8),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, end_index = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert end_index == expected_end