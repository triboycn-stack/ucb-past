# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 2, 迭代: 5
# 生成时间: 2026-05-23 09:16:09

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符的情况
    ('"he\\\"llo"', 1, True, ['he"llo'], 8),
    # 转义字符不是双引号
    ('"he\\\\llo"', 1, True, ['he\\llo'], 8),
    # 多个转义字符
    ('"he\\\\\\\"llo"', 1, True, ['he\\"llo'], 10),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 未闭合的字符串（应抛出异常）
    ('"hello', 1, True, None, None),
    # 转义字符后没有内容（应抛出异常）
    ('"\\', 1, True, None, None),
    # 转义字符无效
    ('"h\\xello"', 1, True, None, None),
    # 边界情况：字符串长度为1
    ('"a"', 1, True, ['a'], 2),
    # 多次循环处理
    ('"h\\\"e\\\\llo"', 1, True, ['h"e\\llo'], 10),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, end_result = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert end_result == expected_end