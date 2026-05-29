# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 1, 迭代: 7
# 生成时间: 2026-04-18 16:40:01

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 转义字符错误
    ('"hello\\x"', 1, True, None, None),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 空字符串（非法）
    ('""', 1, True, None, None),
    # 未闭合的字符串
    ('"hello', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 长字符串
    ('"a" * 100', 1, True, ['a' * 100], 2 + len('a' * 100)),
    # 转义字符后无内容
    ('"\\\\"', 1, True, ['\\'], 4),
    # 转义字符后有其他字符
    ('"\\x"', 1, True, None, None),
    # 多次循环处理
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        parts = result.split('\n') if '\n' in result else [result]
        assert parts == expected_parts
        assert final_end == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None