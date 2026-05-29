# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not name)
# 重复次数: 0, 迭代: 10
# 生成时间: 2026-04-18 17:03:16

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 条件分支测试：not name
    ("", False),
    # 条件分支测试：正则表达式匹配失败
    ("123invalid", False),
    ("1var", False),
    ("invalid@name", False),
    # 条件分支测试：正则表达式匹配成功，但属于保留字
    ("class", False),
    ("function", False),
    ("let", False),
    ("const", False),
    # 条件分支测试：正则表达式匹配成功，且不属于保留字
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("myVar", True),
    # 边界情况：最小长度
    ("a", True),
    # 边界情况：最大长度（假设为100字符）
    ("x" * 100, True),
    # 特殊字符测试
    ("valid_name", True),
    ("valid-name", False),
    ("valid.name", False),
    # 多个保留字测试
    ("break", False),
    ("case", False),
    ("catch", False),
    ("default", False),
    ("delete", False),
    ("do", False),
    ("else", False),
    ("export", False),
    ("extends", False),
    ("finally", False),
    ("for", False),
    ("if", False),
    ("in", False),
    ("instanceof", False),
    ("new", False),
    ("return", False),
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
    ("static", False),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected