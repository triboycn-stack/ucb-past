# 方法: PAST
# 目标文件: target7_closure.py
# 条件路径: not (not re.match('^[a-zA-Z_$][a-zA-Z0-9_$]*$', name))
# 重复次数: 3, 迭代: 8
# 生成时间: 2026-04-18 17:08:56

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
    ("_abc", True),
    ("$abc", True),
    ("abc123", True),
    # 无效标识符（开头错误）
    ("123invalid", False),
    ("1var", False),
    ("2ndVar", False),
    # 无效标识符（包含非法字符）
    ("invalid-name", False),
    ("invalid name", False),
    ("invalid@name", False),
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
    # 特殊情况
    ("__proto__", True),  # 不是保留字
    ("__proto", True),
    ("_prototype", True),
    ("$", True),
    ("_", True),
    # 含有数字的合法标识符
    ("var1", True),
    ("var_1", True),
    ("var$1", True),
    # 含有下划线和美元符号的合法标识符
    ("var_name", True),
    ("var$name", True),
    # 非法标识符（空字符串）
    ("", False),
    # 非法标识符（仅数字）
    ("123", False),
    # 非法标识符（以美元符号开头但后续有非法字符）
    ("$123abc", True),
    ("$abc123", True),
    ("$abc_123", True),
    ("$abc$123", True),
    # 非法标识符（以美元符号开头但包含非法字符）
    ("$abc#123", False),
    ("$abc@123", False),
])
def test_is_valid_js_identifier(name, expected):
    result = is_valid_js_identifier(name)
    assert result == expected