# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name)
# 重复次数: 3, 迭代: 7
# 生成时间: 2026-04-18 17:08:46

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 有效标识符
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("_var", True),
    ("$var", True),
    ("abc", True),
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
    ("2ndVar", False),
    # 无效标识符（包含非法字符）
    ("invalid@name", False),
    ("invalid#name", False),
    ("invalid name", False),
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
    # 特殊情况
    ("__proto__", True),
    ("_constructor", True),
    ("$123", True),
    ("_123", True),
    ("$123_", True),
    # 非法输入
    (123, False),
    (None, False),
    (True, False),
    (False, False),
    ([], False),
    ({}, False),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected