# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (content)
# 重复次数: 4, 迭代: 7
# 生成时间: 2026-04-26 06:25:40

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    ("  abc\n  def\n  ghi", "abc\ndef\nghi"),
    # 空行处理
    ("  \n  abc\n  ", "  \nabc\n  "),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行
    ("   \n   \n   ", "   \n   \n   "),
    # 非空行的最小缩进为0
    ("abc\n  def", "abc\n  def"),
    # 非空行的最小缩进为1
    (" a\n  b\n c", "a\n b\nc"),
    # 边界情况：单行
    ("  single line", "single line"),
    ("single line", "single line"),
    # 边界情况：多行
    ("  line1\n  line2\n  line3", "line1\nline2\nline3"),
    # 含制表符
    ("\t\ttabbed\n\t\tcontent", "tabbed\ncontent"),
    # 含混合空格和制表符
    ("  \t  mixed\n  \t  content", "mixed\ncontent"),
    # 异常情况：非字符串输入
    (123, 123),
    (None, None),
    # 异常情况：空字符串
    ("", ""),
    # 条件分支测试：content为空的情况
    ("   \n  abc", "   \nabc"),
    ("   \n   \n  abc", "   \n   \nabc"),
    # 循环测试：空集合（无非空行）
    ("   \n   \n   ", "   \n   \n   "),
    # 循环测试：单元素
    ("  abc", "abc"),
    # 循环测试：多元素
    ("  a\n  b\n  c", "a\nb\nc"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected