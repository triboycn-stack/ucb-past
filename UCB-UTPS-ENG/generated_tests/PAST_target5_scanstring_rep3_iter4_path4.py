# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 3, 迭代: 4
# 生成时间: 2026-05-23 09:22:30

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello", 0, True, ["hello"], 5),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 转义字符错误
    ('"hello\\"', 1, True, [], -1),
    # 字符串未闭合
    ('"hello', 0, True, [], -1),
    # 空字符串
    ('""', 0, True, [''], 1),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 14),
    # 转义后非引号
    ('"hello\\a"', 1, True, [], -1),
    # 边界情况：字符串长度为1
    ('"a"', 0, True, ['a'], 1),
    # 转义后是引号
    ('"hello\\"world"', 1, True, ['hello"world'], 14),
    # 转义后是反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 14),
    # 长字符串
    ('"a" * 100', 1, True, ['a' * 100], 102),
    # 无转义字符的多段字符串
    ('"hello world"', 1, True, ['hello world'], 12),
    # 混合转义和普通字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert final_end == expected_end
    except ValueError:
        assert expected_end == -1