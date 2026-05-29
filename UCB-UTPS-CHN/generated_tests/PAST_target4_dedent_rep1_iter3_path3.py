# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (line and len(line) >= margin)
# 重复次数: 1, 迭代: 3
# 生成时间: 2026-05-23 09:00:22

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\nworld"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc\n  def", "\nabc\ndef"),
    # 没有非空行
    ("   \n   ", "   \n   "),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 仅有一行
    ("   test", "test"),
    # 无缩进
    ("hello\nworld", "hello\nworld"),
    # 不同缩进
    ("  a\n   b\n  c", "a\nb\nc"),
    # 边界情况：margin为0
    ("a\nb\nc", "a\nb\nc"),
    # 边界情况：margin为最大值
    ("      a\n      b", "a\nb"),
    # 非空行但没有缩进
    ("a\n  b\n   c", "a\nb\nc"),
    # 有空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 非空行但缩进不同
    ("  a\n   b\n  c", "a\nb\nc"),
    # 非空行但缩进为0
    ("a\n  b\n   c", "a\nb\nc"),
    # 非空行但缩进为最大
    ("      a\n      b", "a\nb"),
    # 非空行但缩进为最小
    ("   a\n   b", "a\nb"),
    # 仅有一个非空行
    ("   abc", "abc"),
    # 多个非空行，缩进相同
    ("   a\n   b\n   c", "a\nb\nc"),
    # 多个非空行，缩进不同
    ("   a\n    b\n   c", "a\nb\nc"),
    # 含有制表符
    ("\t\thello\n\t\tworld", "hello\nworld"),
    # 含有混合空格和制表符
    ("  \t  a\n  \t  b", "a\nb"),
    # 非法输入（非字符串）
    (123, 123),
    (None, None),
    # 空字符串
    ("", ""),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected