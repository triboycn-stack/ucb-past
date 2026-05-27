# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: comment.startswith('@param')
# 重复次数: 0, 迭代: 4
# 生成时间: 2026-04-08 09:45:59

import pytest
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    ("validName", True),
    ("_private", True),
    ("my_var", True),
    ("123invalid", False),
    ("class", False),
    ("", False),
    ("123", False),
    ("$var", True),
    ("with", False),
    ("yield", False),
    ("let", False),
    ("static", False),
    ("function", False),
    ("return", False),
    ("super", False),
    ("this", False),
    ("new", False),
    ("delete", False),
    ("in", False),
    ("instanceof", False),
    ("export", False),
    ("import", False),
    ("extends", False),
    ("implements", True),
    ("interface", True),
    ("package", True),
    ("protected", True),
    ("private", True),
    ("public", True),
    ("abstract", True),
    ("boolean", True),
    ("byte", True),
    ("char", True),
    ("double", True),
    ("float", True),
    ("int", True),
    ("long", True),
    ("short", True),
    ("void", False),
    ("undefined", True),
    ("NaN", True),
    ("Infinity", True),
    ("null", True),
    ("true", True),
    ("false", True),
])
def test_is_valid_js_identifier(name, expected):
    assert is_valid_js_identifier(name) == expected