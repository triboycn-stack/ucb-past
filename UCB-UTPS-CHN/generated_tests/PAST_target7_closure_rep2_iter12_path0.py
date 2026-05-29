# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name))
# 重复次数: 2, 迭代: 12
# 生成时间: 2026-04-18 17:07:28

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
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
    ("2test", False),
    # 无效标识符（包含非法字符）
    ("test@name", False),
    ("test#name", False),
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
    ("_", True),
    ("$", True),
    ("_123", True),
    ("$123", True),
    ("_abc123", True),
    ("$abc123", True),
    # 无效标识符（空字符串）
    ("", False),
    # 无效标识符（仅数字）
    ("123", False),
    # 无效标识符（包含特殊字符）
    ("test-name", False),
    ("test name", False),
    ("test.name", False),
    # 保留字边界情况
    ("BREAK", False),
    ("Break", False),
    ("bReAk", False),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected