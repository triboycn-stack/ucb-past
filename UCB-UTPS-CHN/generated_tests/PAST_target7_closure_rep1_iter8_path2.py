# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not name)
# 重复次数: 1, 迭代: 8
# 生成时间: 2026-04-18 17:04:59

import pytest
import re
from target7_closure import is_valid_js_identifier

@pytest.mark.parametrize("name,expected", [
    # 条件分支测试：not name
    ("", False),
    # 条件分支测试：正则匹配失败
    ("123invalid", False),
    ("1var", False),
    ("invalid@name", False),
    # 条件分支测试：正则匹配成功，但属于保留字
    ("class", False),
    ("function", False),
    ("let", False),
    ("const", False),
    # 条件分支测试：正则匹配成功，且不是保留字
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("myVar", True),
    # 边界情况：最小长度
    ("a", True),
    # 边界情况：最大长度（假设为100字符）
    ("x" * 100, True),
    # 特殊情况：包含下划线和美元符号
    ("_underscore$", True),
    ("$dollar_", True),
    # 异常情况：非字符串输入（虽然函数参数是str类型，但测试传入其他类型）
    (123, False),
    (None, False),
    ([], False),
    # 循环测试：保留字集合
    ("break", False),
    ("case", False),
    ("catch", False),
    ("default", False),
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
    ("let", False),
    ("static", False),
])
def test_is_valid_js_identifier(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected