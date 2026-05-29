# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: line and len(line) >= margin
# 重复次数: 1, 迭代: 2
# 生成时间: 2026-05-23 09:00:14

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc\n  ", "  \nabc\n  "),
    # 没有非空行
    ("   \n   ", "   \n   "),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 仅有一行
    ("   test", "test"),
    # 无缩进
    ("hello", "hello"),
    # 边界情况：margin为0
    ("   \n  a\n   b", "   \n  a\n   b"),
    # 有前导空格但没有内容的行
    ("   \n  \n   ", "   \n  \n   "),
    # 多个不同缩进的行
    ("  a\n   b\n    c", "a\nb\nc"),
    # 非空行但缩进不同
    ("  a\n   b\n  c", "a\nb\nc"),
    # 有换行符但没有内容
    ("  \n\n  ", "  \n\n  "),
    # 非法输入（非字符串）
    (123, 123),
    # 字符串包含特殊字符
    ("  !@#$%^&*\n  abc123", "!@#$%^&*\nabc123"),
    # 超长字符串
    (" " * 100 + "test", "test"),
    # 临界值：margin等于行长度
    ("  abc\n  def", "abc\ndef"),
    # 临界值：margin大于行长度
    ("  abc\n   def", "abc\n def"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected