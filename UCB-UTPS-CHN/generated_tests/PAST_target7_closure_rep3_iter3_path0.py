# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name))
# 重复次数: 3, 迭代: 3
# 生成时间: 2026-04-18 17:08:15

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 有效标识符
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("x" * 100, True),
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
    ("#invalid", False),
    # 无效标识符（包含非法字符）
    ("invalid@name", False),
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
    # 空字符串
    ("", False),
    # 单字符
    ("a", True),
    ("_", True),
    ("$", True),
    # 多字符
    ("abc123", True),
    ("_abc", True),
    ("$abc", True),
    # 特殊情况
    ("__proto__", True),
    ("__defineGetter__", True),
    ("__defineSetter__", True),
    ("constructor", True),
    ("hasOwnProperty", True),
    ("isPrototypeOf", True),
    ("propertyIsEnumerable", True),
    ("toLocaleString", True),
    ("toString", True),
    ("valueOf", True),
    # 非法输入
    (123, False),
    (None, False),
    (True, False),
    (False, False),
    ([], False),
    ({}, False),
])
def test_is_valid_js_identifier(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected