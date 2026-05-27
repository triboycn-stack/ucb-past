# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: line and len(line) >= margin
# 重复次数: 2, 迭代: 2
# 生成时间: 2026-04-26 06:22:46

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\nworld"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc\n  def", "\nabc\ndef"),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行
    ("   \n   \n   ", "   \n   \n   "),
    # 仅有一行
    ("  line", "line"),
    # 多行，不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    # 边界情况：margin为0
    ("hello\nworld", "hello\nworld"),
    # 边界情况：margin为最大值
    ("          \n          ", "          \n          "),
    # 非空行没有缩进
    ("hello\nworld", "hello\nworld"),
    # 含有制表符
    ("\t\thello\n\t\tworld", "hello\nworld"),
    # 混合空格和制表符
    ("  \t  hello\n  \t  world", "hello\nworld"),
    # 异常输入
    (None, None),
    (123, 123),
    (["  a", "  b"], ["  a", "  b"]),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected