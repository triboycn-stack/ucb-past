# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '"'
# 重复次数: 4, 迭代: 2
# 生成时间: 2026-04-18 16:45:07

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试 esc == '"'
    ('"hello\"world"', 1, True, ['hello"world'], 12),
    # 测试正常字符串结束
    ('"hello world"', 1, True, ['hello world'], 12),
    # 测试转义字符
    ('"hello\\"world"', 1, True, ['hello"world'], 13),
    # 测试多转义字符
    ('"hello\\"world\\t"', 1, True, ['hello"world\t'], 15),
    # 测试空字符串（非法）
    ('""', 1, True, [], 1),
    # 测试未终止字符串（抛出异常）
    ('"hello', 1, True, None, None),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 测试多部分拼接
    ('"a\\"b\\tc"', 1, True, ['a"b\tc'], 8),
    # 测试转义后继续处理
    ('"a\\"b\\\\c"', 1, True, ['a"b\\c'], 9),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        parts = result.split('\n') if '\n' in result else [result]
        assert parts == expected_parts
        assert new_end == expected_end
    except ValueError as e:
        if expected_parts is None and expected_end is None:
            assert str(e) == "Unterminated string"
        else:
            raise e