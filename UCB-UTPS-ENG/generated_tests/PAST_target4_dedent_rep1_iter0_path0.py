# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None or indent < margin
# 重复次数: 1, 迭代: 0
# 生成时间: 2026-05-23 09:00:00

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc\n  def", "\nabc\ndef"),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行
    ("   \n   \n   ", "   \n   \n   "),
    # 单行非空
    ("   test", "test"),
    # 多行非空，不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    # 边界情况：margin为0
    ("hello\nworld", "hello\nworld"),
    # 边界情况：margin为最大值
    ("        abc", "abc"),
    # 非空行无缩进
    ("abc\ndef", "abc\ndef"),
    # 首行为空
    ("\n  abc\n  def", "\nabc\ndef"),
    # 尾行为空
    ("  abc\n  def\n", "abc\ndef\n"),
    # 混合空行和非空行
    ("  a\n\n  b\n  c", "a\n\nb\nc"),
    # 非法输入（非字符串）
    (123, 123),
    # 异常情况：包含特殊字符
    ("  !@#$%^&*()\n  abc", "!@#$%^&*()\nabc"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected