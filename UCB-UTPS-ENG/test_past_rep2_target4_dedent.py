import sys, os
sys.path.insert(0, os.getcwd())
from target4_dedent import *

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    ("  abc\n  def\n  ghi", "abc\ndef\nghi"),
    # 空行处理
    ("  \n  \n  ", "\n\n"),
    ("  \n  abc\n  ", "\nabc\n"),
    # 没有非空行的情况
    ("   \n   \n   ", "   \n   \n   "),
    # 单行情况
    ("   line", "line"),
    ("line", "line"),
    # 多行不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    ("   a\n  b\n c", "a\nb\nc"),
    # 边界情况：最大缩进
    (" " * 100 + "hello", "hello"),
    # 异常输入
    (None, None),
    (123, 123),
    (["  a", "  b"], "a\nb"),
    # 条件分支测试
    # margin is None 的情况（所有行都是空行）
    ("   \n   \n   ", "   \n   \n   "),
    # indent < margin 的情况（多行不同缩进）
    ("  a\n   b\n    c", "a\nb\nc"),
    # indent >= margin 的情况（所有行缩进相同或更少）
    ("   a\n   b\n   c", "a\nb\nc"),
    # 循环测试：空集合（无行）
    ("", ""),
    # 单元素循环
    ("  line", "line"),
    # 多元素循环
    ("  a\n  b\n  c", "a\nb\nc"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected
