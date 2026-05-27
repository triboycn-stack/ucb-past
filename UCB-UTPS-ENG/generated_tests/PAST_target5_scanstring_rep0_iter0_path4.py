# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (ch == '\\')
# 重复次数: 0, 迭代: 0
# 生成时间: 2026-04-18 16:36:51

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ("hello", 0, True, ["hello"], 5),
    # 带转义字符的情况
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 转义字符错误
    ('"hello\\"', 1, True, [], -1),
    # 多个转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 14),
    # 空字符串
    ('""', 0, True, [''], 1),
    # 字符串中包含换行
    ('"hello\nworld"', 1, True, ['hello\nworld'], 12),
    # 字符串中包含多个转义
    ('"hello\\\\nworld"', 1, True, ['hello\\nworld'], 14),
    # 未终止的字符串（触发异常）
    ('"hello', 0, True, [], -1),
    # 无效转义字符
    ('"hello\\xworld"', 1, True, [], -1),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 多个部分拼接
    ('"hello\\\"world\\\"test"', 1, True, ['hello"world"test'], 17),
    # 转义后继续处理
    ('"hello\\\\world"', 1, True, ['hello\\world'], 14),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert final_end == expected_end
    except ValueError:
        assert expected_end == -1