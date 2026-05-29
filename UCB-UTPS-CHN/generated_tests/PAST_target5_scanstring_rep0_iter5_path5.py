# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '"')
# 重复次数: 0, 迭代: 5
# 生成时间: 2026-05-23 09:19:29

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 正常情况：字符串正常结束
    ('"hello"', 0, True, ['hello'], 6),
    # 转义字符："\""
    ('"hello\\"world"', 0, True, ['hello"world'], 13),
    # 转义字符：\\
    ('"hello\\\\world"', 0, True, ['hello\\world'], 13),
    # 转义字符：其他（触发异常）
    ('"hello\\xworld"', 0, True, None, None),
    # 多个转义字符
    ('"hello\\"world\\\\test"', 0, True, ['hello"world\\test'], 17),
    # 空字符串（错误）
    ('""', 0, True, None, None),
    # 未终止字符串（错误）
    ('"hello', 0, True, None, None),
    # 边界情况：单个字符
    ('"a"', 0, True, ['a'], 2),
    # 边界情况：多个转义
    ('"a\\\\b\\\\c"', 0, True, ['a\\b\\c'], 9),
    # 非转义字符
    ('"abc def"', 0, True, ['abc def'], 8),
    # 包含换行符
    ('"hello\nworld"', 0, True, ['hello\nworld'], 11),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts)
        assert new_end == expected_end