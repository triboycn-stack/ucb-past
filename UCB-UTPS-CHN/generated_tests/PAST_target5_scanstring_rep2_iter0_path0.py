# 方法: PAST
# 目标文件: target5_scanstring.py
# 条件路径: esc == '\\'
# 重复次数: 2, 迭代: 0
# 生成时间: 2026-05-23 09:20:52

import pytest
from target5_scanstring import scanstring

@pytest.mark.parametrize("s, end, strict, expected_parts, expected_end", [
    # 测试转义字符 \\ 的情况
    ('hello\\world', 0, True, ['hello\\world'], 11),
    # 测试转义字符 \" 的情况
    ('hello\\"world', 0, True, ['hello"world'], 11),
    # 测试转义字符 \n 的情况（虽然代码中未处理，但测试逻辑）
    ('hello\\nworld', 0, True, ['hello\\nworld'], 11),
    # 测试空字符串
    ('', 0, True, [], 0),
    # 测试单个字符
    ('a', 0, True, ['a'], 1),
    # 测试多个转义字符
    ('hello\\\\world', 0, True, ['hello\\world'], 12),
    # 测试转义字符后有其他字符
    ('hello\\tworld', 0, True, ['hello\\tworld'], 11),
    # 测试转义字符后没有字符（错误情况）
    ('hello\\', 0, True, ['hello\\'], 6),
    # 测试字符串中间有转义字符
    ('h\\e\\l\\l\\o', 0, True, ['h\\e\\l\\l\\o'], 9),
    # 测试字符串中有多个转义字符
    ('a\\b\\c', 0, True, ['a\\b\\c'], 6),
    # 测试字符串中包含转义和普通字符混合
    ('abc\\def', 0, True, ['abc\\def'], 7),
    # 测试字符串以转义字符结尾
    ('abc\\', 0, True, ['abc\\'], 4),
    # 测试字符串中包含多个转义字符
    ('a\\b\\c\\d', 0, True, ['a\\b\\c\\d'], 8),
    # 测试字符串中包含转义和非转义字符
    ('a\\b c', 0, True, ['a\\b c'], 6),
    # 测试字符串中包含转义和特殊字符
    ('a\\b!@#$', 0, True, ['a\\b!@#$', 6]),
])
def test_scanstring_core_logic(s, end, strict, expected_parts, expected_end):
    result = scanstring(s, end, strict)
    assert result[0] == ''.join(expected_parts)
    assert result[1] == expected_end