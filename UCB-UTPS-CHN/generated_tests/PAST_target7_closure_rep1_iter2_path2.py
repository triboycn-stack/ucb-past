# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not name)
# 重复次数: 1, 迭代: 2
# 生成时间: 2026-04-26 06:47:51

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
    ("with$", True),
    ("thisIsAValid", True),
    # 保留字边界测试
    ("yield", False),
    ("export", False),
    # 非法输入测试
    (123, False),
    (None, False),
    ([], False),
    ({}, False),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected