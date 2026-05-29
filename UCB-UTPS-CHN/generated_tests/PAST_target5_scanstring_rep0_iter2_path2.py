# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 0, 迭代: 2
# 生成时间: 2026-05-23 09:19:07

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符处理
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后无内容
    ('"hello\\"', 1, True, ['hello"'], 7),
    # 转义字符后有其他字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 空字符串（错误情况）
    ('""', 1, True, [], 1),
    # 未终止字符串（错误情况）
    ('"hello', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 多个转义字符
    ('"a\\\\b\\\"c"', 1, True, ['a\\b"c'], 9),
    # 转义字符后没有结束引号（错误）
    ('"hello\\', 1, True, None, None),
    # 转义字符无效
    ('"hello\\x"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert new_end == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None