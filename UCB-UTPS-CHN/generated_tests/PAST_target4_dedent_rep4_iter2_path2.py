# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: line and len(line) >= margin
# 重复次数: 4, 迭代: 2
# 生成时间: 2026-04-26 06:24:59

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
    ("   \n   ", "   \n   "),
    # 仅有一行
    ("  test", "test"),
    # 边界情况：margin为0
    ("test\n  line", "test\n  line"),
    # 边界情况：margin为最大值
    ("        abc", "abc"),
    # 条件分支测试：line and len(line) >= margin
    ("  a\n b", "a\nb"),
    ("  a\n  b", "a\nb"),
    # 异常情况：非字符串输入
    (123, 123),
    (None, None),
    # 特殊字符
    ("  !@#$\n  %^&*", "!@#$\n%&*"),
    # 多种缩进混合
    ("  a\n   b\n  c", "a\nb\nc"),
    # 首行为空
    ("\n  abc\n  def", "\nabc\ndef"),
    # 尾行为空
    ("  abc\n  def\n", "abc\ndef\n"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected