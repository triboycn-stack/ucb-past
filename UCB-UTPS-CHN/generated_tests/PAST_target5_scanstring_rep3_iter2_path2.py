# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: ch == '\\'
# 重复次数: 3, 迭代: 2
# 生成时间: 2026-05-23 09:22:14

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符处理
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 转义字符后没有结束引号（异常）
    ('"hello\\', 1, True, None, None),
    # 空字符串（异常）
    ('"', 0, True, None, None),
    # 字符串中间有转义
    ('"h\\\"ello"', 1, True, ['h"ello'], 8),
    # 多次循环处理
    ('"a\\nb\\tc\\td"', 1, True, ['a\nb\tc\td'], 10),
    # 边界情况：字符串长度为1
    ('"a"', 1, True, ['a'], 2),
    # 非法输入：end超出范围
    ('"abc"', 5, True, None, None),
    # 严格模式下非法转义
    ('"hello\\x"', 1, True, None, None),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        parts = result
        assert parts == expected_parts
        assert new_end == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None