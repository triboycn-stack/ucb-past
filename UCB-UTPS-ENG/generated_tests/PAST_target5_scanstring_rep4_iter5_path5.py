# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 4, 迭代: 5
# 生成时间: 2026-05-23 09:23:40

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串正常结束
    ('"hello"', 1, True, ['hello'], 6),
    # 转义字符：转义双引号
    ('"he\\\"llo"', 1, True, ['he"llo'], 8),
    # 转义字符：转义反斜杠
    ('"he\\\\llo"', 1, True, ['he\\llo'], 8),
    # 转义字符：无效转义
    ('"he\\x llo"', 1, True, None, None),
    # 字符串中间有多个转义
    ('"he\\\"llo\\\\world"', 1, True, ['he"llo\\world'], 14),
    # 空字符串（错误）
    ('""', 1, True, None, None),
    # 未终止字符串（错误）
    ('"hello', 1, True, None, None),
    # 多个转义字符处理
    ('"a\\nb\\tc\\rd"', 1, True, ['a\nb\tc\rd'], 10),
    # 边界情况：字符串长度为1
    ('"\\"', 1, True, ['"'], 3),
    # 边界情况：字符串长度为2（包含转义）
    ('"\\\\"', 1, True, ['\\'], 4),
    # 非严格模式下忽略非法转义
    ('"he\\x llo"', 1, False, ['he\\x llo'], 7),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end