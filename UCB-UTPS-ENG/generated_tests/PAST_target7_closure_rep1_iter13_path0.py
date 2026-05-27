# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name))
# 重复次数: 1, 迭代: 13
# 生成时间: 2026-04-18 17:05:41

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
    ("x" * 100, True),  # 长字符串
    # 特殊字符
    ("_underscore", True),
    ("$dollar", True),
    ("_123", True),
    ("__", True),
    ("$$", True),
    # 无效标识符（包含非法字符）
    ("invalid-char!", False),
    ("invalid char", False),
    ("invalid:char", False),
    ("invalid[char]", False),
    # 保留字与合法字符组合
    ("classTest", False),
    ("returnVal", False),
    ("ifElse", False),
    # 空白字符
    (" ", False),
    ("\t", False),
    ("\n", False),
    # 多个保留字组合
    ("breakCase", False),
    ("functionReturn", False),
    # 合法但保留字的变体
    ("Class", True),
    ("RETURN", True),
    ("If", True),
])
def test_is_valid_js_identifier(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected