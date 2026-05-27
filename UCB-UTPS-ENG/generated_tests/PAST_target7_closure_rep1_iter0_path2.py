# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not name)
# 重复次数: 1, 迭代: 0
# 生成时间: 2026-04-18 17:03:56

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
    # 条件分支测试：正则表达式匹配成功，且不是保留字
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
    ("with", False),
    ("yield", False),
    ("in", False),
    # 多元素保留字集合测试
    ("static", False),
    ("export", False),
    ("extends", False),
    # 空白字符测试
    (" ", False),
    ("\t", False),
    ("\n", False),
    # 非ASCII字符测试
    ("café", False),
    ("résumé", False),
    # 混合合法与非法字符
    ("validName123", True),
    ("invalid-name", False),
    ("valid_name", True),
    ("invalid.name", False),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected