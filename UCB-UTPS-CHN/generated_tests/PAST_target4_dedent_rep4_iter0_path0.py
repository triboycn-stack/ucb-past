# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None or indent < margin
# 重复次数: 4, 迭代: 0
# 生成时间: 2026-04-26 06:24:44

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
    (" " * 100 + "text", "text"),
    # 异常情况：非字符串输入
    (123, 123),
    (None, None),
    # 特殊字符
    ("  !@#$%^&*\n  abc", "!@#$%^&*\nabc"),
    # 空字符串
    ("", ""),
    # 只有空行
    ("   \n   \n   ", "   \n   \n   "),
    # 混合空行和非空行
    ("   \n  abc\n   \n  def", "\nabc\n\ndef"),
    # 缩进为0的情况
    ("abc\n  def", "abc\n  def"),
    # 多个非空行，不同缩进
    ("  a\n   b\n  c", "a\nb\nc"),
    # 首行为空
    ("  \n  abc\n  def", "\nabc\ndef"),
    # 尾行为空
    ("  abc\n  def\n  ", "abc\ndef\n"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected