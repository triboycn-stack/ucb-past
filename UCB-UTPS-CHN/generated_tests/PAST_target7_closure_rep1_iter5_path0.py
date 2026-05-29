# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name))
# 重复次数: 1, 迭代: 5
# 生成时间: 2026-04-18 17:04:35

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 有效标识符
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("this", False),  # 保留字
    ("function", False),  # 保留字
    ("let", False),  # 保留字
    ("const", False),  # 保留字
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
    ("#invalid", False),
    ("@invalid", False),
    # 空字符串
    ("", False),
    # 单字符
    ("a", True),
    ("_", True),
    ("$", True),
    # 多字符
    ("abc123", True),
    ("abc_123", True),
    ("abc$123", True),
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
    ("x" * 100, True),
    ("x" * 101, True),  # 超过100字符，但符合正则表达式
    ("x" * 255, True),
    # 特殊字符
    ("abc!def", False),
    ("abc@def", False),
    ("abc#def", False),
    ("abc%def", False),
    ("abc^def", False),
    ("abc&def", False),
    ("abc*def", False),
    ("abc+def", False),
    ("abc=def", False),
    ("abc?def", False),
    ("abc/def", False),
    ("abc|def", False),
    ("abc\\def", False),
    ("abc: def", False),
    ("abc;def", False),
    ("abc<def", False),
    ("abc>def", False),
    ("abc[def", False),
    ("abc]def", False),
    ("abc{def", False),
    ("abc}def", False),
    ("abc~def", False),
    ("abc`def", False),
    ("abc^def", False),
    ("abc\"def", False),
    ("abc'def", False),
    # 混合情况
    ("_valid123", True),
    ("$valid123", True),
    ("valid123_", True),
    ("valid123$", True),
    ("valid123_abc", True),
    ("valid123$abc", True),
    ("valid123_abc$", True),
    ("valid123$abc_", True),
])
def test_is_valid_js_identifier(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected