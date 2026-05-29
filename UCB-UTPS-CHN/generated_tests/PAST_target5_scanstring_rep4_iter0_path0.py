# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 4, 迭代: 0
# 生成时间: 2026-05-23 09:23:04

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试正常情况，包含转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 12),
    # 测试转义字符为反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 测试转义字符为其他字符（触发异常）
    ('"hello\\xworld"', 1, True, None, None),
    # 测试字符串结束在转义字符后
    ('"hello\\', 1, True, None, None),
    # 测试空字符串
    ('""', 1, True, [''], 2),
    # 测试多段字符串
    ('"hello\\\"world\\\"test"', 1, True, ['hello"world"test'], 16),
    # 测试未终止字符串
    ('"hello', 1, True, None, None),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 测试带多个转义字符的字符串
    ('"hello\\\\\\\"world"', 1, True, ['hello\\"world'], 14),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, final_end = scanstring(s, end, strict)
        parts = result
        assert parts == ''.join(expected_parts) if expected_parts else True
        assert final_end == expected_end
    except ValueError:
        assert expected_parts is None and expected_end is None