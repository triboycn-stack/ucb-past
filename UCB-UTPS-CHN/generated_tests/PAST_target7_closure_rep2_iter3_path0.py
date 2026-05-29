# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name))
# 重复次数: 2, 迭代: 3
# 生成时间: 2026-04-18 17:06:20

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 有效标识符
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("abc", True),
    ("x" * 100, True),
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
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
    ("_", True),
    ("$", True),
    ("_", True),
    ("__", True),
    ("_$", True),
    ("_1", True),
    ("1", False),
    ("_", True),
    # 特殊字符
    ("a-b", False),
    ("a b", False),
    ("a.b", False),
    ("a[b]", False),
    # 非法输入
    (123, False),
    (None, False),
    (True, False),
    (False, False),
    (["invalid"], False),
    ({"invalid": "value"}, False),
])
def test_is_valid_js_identifier(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected