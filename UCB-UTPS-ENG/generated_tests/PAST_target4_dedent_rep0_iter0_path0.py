# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None or indent < margin
# 重复次数: 0, 迭代: 0
# 生成时间: 2026-05-23 08:59:04

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  \n  ", "\n\n"),
    # 没有非空行
    ("   \n   ", "\n"),
    # 所有行都是空行
    ("   \n   \n   ", "\n\n"),
    # 单行非空
    ("   line", "line"),
    # 多行不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    # 首行是空行
    ("  \n  abc", "abc"),
    # 尾行是空行
    ("abc  \n  ", "abc  "),
    # 边界情况：最小缩进
    ("a", "a"),
    ("  a", "a"),
    ("   a", "a"),
    # 边界情况：最大缩进
    ("        a", "a"),
    # 异常输入
    (None, None),
    (123, 123),
    (["list"], ["list"]),
    # 特殊字符
    ("  !@#$%^&*()\n    test", "!@#$%^&*\ntest"),
    # 混合空行和非空行
    ("  \n  abc\n  \n  def", "abc\ndef"),
    # 无任何缩进
    ("hello\nworld", "hello\nworld"),
    # 仅有一个非空行
    ("   line   ", "line   "),
    # 有多个非空行，但缩进相同
    ("  a\n  b\n  c", "a\nb\nc"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected