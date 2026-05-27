# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: content
# 重复次数: 0, 迭代: 6
# 生成时间: 2026-05-23 08:59:45

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\nworld"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc\n  def", "\nabc\ndef"),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行
    ("   \n   \n   ", "   \n   \n   "),
    # 单个非空行
    ("   abc", "abc"),
    # 多个非空行，不同缩进
    ("  abc\n   def\n  ghi", "abc\ndef\nghi"),
    # 边界情况：最小缩进
    ("a\nb\nc", "a\nb\nc"),
    # 边界情况：最大缩进（超过行长度）
    ("   abc\n   def", "abc\ndef"),
    # 非空行前有空格，但行本身为空
    ("   \n   \n   ", "   \n   \n   "),
    # 含有制表符
    ("\t\thello\n\t\tworld", "hello\nworld"),
    # 含有混合空格和制表符
    ("  \t  abc\n  \t  def", "abc\ndef"),
    # 异常输入
    (None, None),
    (123, 123),
    (["  a", "  b"], ["  a", "  b"]),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected