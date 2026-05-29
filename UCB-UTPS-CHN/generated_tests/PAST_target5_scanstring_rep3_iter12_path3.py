# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '"'
# 重复次数: 3, 迭代: 12
# 生成时间: 2026-04-18 16:44:33

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试 esc == '"'
    ('"hello\"world"', 1, True, ['hello"world'], 12),
    # 测试正常字符串结束
    ('"hello world"', 1, True, ['hello world'], 12),
    # 测试转义字符
    ('"hello\\\"world"', 1, True, ['hello"world'], 13),
    # 测试空字符串（应抛出异常）
    ('"', 0, True, None, None),
    # 测试未终止字符串
    ('"hello', 1, True, None, None),
    # 测试多转义字符
    ('"hello\\\\world"', 1, True, ['hello\\world'], 13),
    # 测试多个转义字符
    ('"hello\\\\\"world"', 1, True, ['hello\\"world'], 14),
    # 测试边界情况：单个字符
    ('"a"', 1, True, ['a'], 2),
    # 测试长字符串
    ('"this is a very long string with many characters"', 1, True, ['this is a very long string with many characters'], 46),
    # 测试转义字符后继续处理
    ('"hello\\\"world\\\"test"', 1, True, ['hello"world"test'], 17),
])
def test_scanstring(s, end, strict, expected_parts, expected_end):
    if expected_parts is None:
        with pytest.raises(ValueError):
            scanstring(s, end, strict)
    else:
        result, result_end = scanstring(s, end, strict)
        assert ''.join(expected_parts) == result
        assert expected_end == result_end