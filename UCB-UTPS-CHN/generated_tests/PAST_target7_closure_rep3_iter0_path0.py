# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name))
# 重复次数: 3, 迭代: 0
# 生成时间: 2026-04-26 06:48:40

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 有效标识符
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("_abc123", True),
    ("abc$", True),
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
    ("2test", False),
    ("#invalid", False),
    ("@invalid", False),
    # 保留字
    ("break", False),
    ("case", False),
    ("catch", False),
    ("class", False),
    ("const", False),
    ("continue", False),
    ("debugger", False),
    ("default", False),
    ("delete", False),
    ("do", False),
    ("else", False),
    ("export", False),
    ("extends", False),
    ("finally", False),
    ("for", False),
    ("function", False),
    ("if", False),
    ("import", False),
    ("in", False),
    ("instanceof", False),
    ("new", False),
    ("return", False),
    ("super", False),
    ("switch", False),
    ("this", False),
    ("throw", False),
    ("try", False),
    ("typeof", False),
    ("var", False),
    ("void", False),
    ("while", False),
    ("with", False),
    ("yield", False),
    ("let", False),
    ("static", False),
    # 边界情况
    ("", False),
    ("a", True),
    ("x" * 100, True),  # 长字符串
    ("_", True),
    ("$", True),
    # 特殊字符
    ("abc@def", False),
    ("abc#def", False),
    ("abc!def", False),
    # 多个保留字
    ("break", False),
    ("return", False),
    ("function", False),
    # 合法但保留字
    ("class", False),
    ("interface", False),
    ("package", False),
    ("private", False),
    ("protected", False),
    ("public", False),
    ("implements", False),
    ("extends", False),
    ("native", False),
    ("static", False),
    ("abstract", False),
    ("final", False),
    ("synchronized", False),
    ("transient", False),
    ("volatile", False),
    ("enum", False),
])
def test_is_valid_js_identifier(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected