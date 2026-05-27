# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: line and len(line) >= margin
# 重复次数: 0, 迭代: 2
# 生成时间: 2026-05-23 08:59:20

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\n    world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc\n  def", "\nabc\ndef"),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行
    ("   \n   \n   ", "   \n   \n   "),
    # 仅有一个非空行
    ("   abc", "abc"),
    # 多个非空行，不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    # 边界情况：margin为0
    ("abc\ndef", "abc\ndef"),
    # 边界情况：margin为最大值
    ("      abc", "abc"),
    # 非空行前有空格，但长度不足margin
    ("  a\n   b", "a\nb"),
    # 空字符串
    ("", ""),
    # 单行空字符串
    ("   ", "   "),
    # 多行空字符串
    ("   \n   ", "   \n   "),
    # 包含制表符
    ("\t\thello\n\t\tworld", "hello\nworld"),
    # 混合空格和制表符
    ("  \t  abc\n  \t  def", "abc\ndef"),
    # 异常输入
    (None, None),
    (123, 123),
    (["  a", "  b"], ["  a", "  b"]),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected