# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not name)
# 重复次数: 1, 迭代: 4
# 生成时间: 2026-04-18 17:04:25

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
    ("break", False),
    ("function", False),
    ("let", False),
    ("static", False),
    # 条件分支测试：正则表达式匹配成功，且不是保留字
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("thisIsValid", True),
    # 边界情况：最小长度
    ("a", True),
    # 边界情况：最大长度（假设为100字符）
    ("x" * 100, True),
    # 特殊字符测试
    ("with$", True),
    ("yield_", True),
    # 保留字边界测试
    ("while", False),
    ("void", False),
    # 多元素测试（虽然没有循环，但覆盖多个保留字）
    ("class", False),
    ("export", False),
    ("extends", False),
    ("super", False),
    ("new", False),
    ("delete", False),
    ("in", False),
    ("instanceof", False),
    ("typeof", False),
    ("var", False),
    ("const", False),
    ("function", False),
    ("return", False),
    ("throw", False),
    ("try", False),
    ("catch", False),
    ("finally", False),
    ("do", False),
    ("while", False),
    ("for", False),
    ("if", False),
    ("else", False),
    ("switch", False),
    ("case", False),
    ("default", False),
    ("continue", False),
    ("debugger", False),
    ("delete", False),
    ("export", False),
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
    ("void", False),
    ("while", False),
    ("with", False),
    ("yield", False),
    ("let", False),
    ("static", False),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected