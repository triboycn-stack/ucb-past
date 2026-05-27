# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not name)
# 重复次数: 4, 迭代: 5
# 生成时间: 2026-04-18 17:10:24

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 条件分支测试：not name
    ("", False),
    ("validName", True),
    # 正则表达式匹配测试
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("123invalid", False),
    ("1var", False),
    ("invalid-char@", False),
    # 保留字测试
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
    ("a", True),
    ("x" * 100, True),
    # 特殊字符测试
    ("__proto__", True),
    ("_constructor", True),
    ("$123", True),
    ("123$", False),
    # 非法输入
    (123, False),
    (None, False),
    (["invalid"], False),
    ({"name": "invalid"}, False),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected