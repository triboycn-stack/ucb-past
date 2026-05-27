# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not name
# 重复次数: 4, 迭代: 14
# 生成时间: 2026-04-18 17:11:31

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 条件分支测试: not name
    ("", False),
    # 有效标识符
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("abc", True),
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
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
    ("a", True),
    ("x" * 100, True),  # 长字符串
    ("_", True),
    ("$", True),
    # 特殊字符
    ("valid-name", False),
    ("valid.name", False),
    ("valid name", False),
    # 空白字符
    (" ", False),
    ("\t", False),
    ("\n", False),
    # 多个保留字
    ("break", False),
    ("return", False),
    ("function", False),
    # 无保留字
    ("myVar", True),
    ("MyClass", True),
    ("myFunction", True),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected