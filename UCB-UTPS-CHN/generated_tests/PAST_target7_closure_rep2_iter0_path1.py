# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name)
# 重复次数: 2, 迭代: 0
# 生成时间: 2026-04-18 17:05:57

import pytest
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 有效标识符
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("a", True),
    ("x" * 100, True),
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
    ("#invalid", False),
    ("@invalid", False),
    # 无效标识符（包含非法字符）
    ("invalid$name", False),
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
    ("_", True),
    ("$", True),
    ("_", True),
    ("_", True),
    ("_", True),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected