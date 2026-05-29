# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not name)
# 重复次数: 4, 迭代: 2
# 生成时间: 2026-04-26 06:49:27

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
    # 特殊情况：保留字但符合正则
    ("return", False),
    # 特殊情况：空字符串
    ("", False),
    # 特殊情况：仅包含下划线
    ("_", True),
    # 特殊情况：仅包含美元符号
    ("$", True),
    # 特殊情况：保留字的大小写变体（不匹配）
    ("CLASS", False),
    ("Function", False),
])
def test_is_valid_js_identifier(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected