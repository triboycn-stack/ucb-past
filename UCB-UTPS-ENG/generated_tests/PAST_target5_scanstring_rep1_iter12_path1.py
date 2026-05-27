# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: not (esc == '\\')
# 重复次数: 1, 迭代: 12
# 生成时间: 2026-04-18 16:40:43

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 基本情况：正常字符串，无转义
    ('"hello"', 1, True, ['hello'], 6),
    # 带转义字符：双引号
    ('"hello\\"world"', 1, True, ['hello"world'], 12),
    # 带转义字符：反斜杠
    ('"hello\\\\world"', 1, True, ['hello\\world'], 12),
    # 多个转义字符
    ('"hello\\"world\\\\test"', 1, True, ['hello"world\\test'], 15),
    # 空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 未终止的字符串（应抛出异常）
    ('"hello', 1, True, None, None),
    # 转义字符无效
    ('"hello\\x"', 1, True, None, None),
    # 边界情况：单个字符
    ('"a"', 1, True, ['a'], 3),
    # 转义字符在末尾
    ('"hello\\"', 1, True, ['hello"'], 8),
    # 多次循环处理
    ('"a\\nb\\tc\\td"', 1, True, ['a\nb\tc\td'], 10),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    try:
        result, new_end = scanstring(s, end, strict)
        assert result == ''.join(expected_parts), f"Expected parts {expected_parts}, got {result}"
        assert new_end == expected_end, f"Expected end index {expected_end}, got {new_end}"
    except ValueError as e:
        if expected_parts is None:
            assert str(e) == "Unterminated string" or str(e) == "Invalid escape", f"Unexpected error: {e}"
        else:
            raise AssertionError(f"Unexpected error: {e}")