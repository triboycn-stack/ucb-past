# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None or indent < margin
# 重复次数: 3, 迭代: 0
# 生成时间: 2026-04-26 06:23:32

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    ("  abc\n  def\n  ghi", "abc\ndef\nghi"),
    # 空行处理
    ("  \n  \n  ", "  \n  \n  "),
    ("  \n  abc\n  ", "  \nabc\n  "),
    # 没有非空行的情况
    ("   \n   \n   ", "   \n   \n   "),
    # 单行情况
    ("  single line", "single line"),
    ("   single line", "single line"),
    # 多行不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    ("   a\n  b\n c", "a\nb\nc"),
    # 边界情况：最小缩进
    ("a\n  b", "a\nb"),
    ("  a\nb", "a\nb"),
    # 非空行无缩进
    ("hello\nworld", "hello\nworld"),
    # 全部缩进
    ("   \n   \n   ", "   \n   \n   "),
    # 混合空行和非空行
    ("   \n  abc\n   \n  def", "   \nabc\n   \ndef"),
    # 特殊字符
    ("  !@#$%^&*\n  abc123", "!@#$%^&*\nabc123"),
    # 非法输入（非字符串）
    (123, 123),
    (None, None),
    # 空字符串
    ("", ""),
    # 只有空行
    ("\n\n", "\n\n"),
    # 仅一个空行
    ("  \n", "  \n"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected