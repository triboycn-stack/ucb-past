# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not name)
# 重复次数: 2, 迭代: 4
# 生成时间: 2026-04-18 17:06:26

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
    ("const", False),
    # 条件分支测试：正则表达式匹配成功，且不属于保留字
    ("validName", True),
    ("_private", True),
    ("$dollar", True),
    ("a1b2c3", True),
    ("myVar", True),
    # 边界情况：最小值
    ("a", True),
    # 边界情况：最大值（假设为100个字符）
    ("x" * 100, True),
    # 特殊情况：保留字的大小写变体
    ("BREAK", True),
    ("Function", True),
    # 非法输入
    (123, False),
    (None, False),
    # 空白字符串
    (" ", False),
    ("\t", False),
    # 多元素测试（保留字集合）
    ("static", False),
    ("export", False),
    ("extends", False),
    ("super", False),
    ("yield", False),
])
def test_target_path(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected