# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (line and len(line) >= margin)
# 重复次数: 2, 迭代: 3
# 生成时间: 2026-04-26 06:22:54

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\nworld"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc\n  def", "\nabc\ndef"),
    # 没有非空行
    ("   \n   ", "   \n   "),
    # 边界情况：margin为0
    ("hello\nworld", "hello\nworld"),
    # 边界情况：margin为最大值
    ("        abc", "abc"),
    # 条件分支测试：line and len(line) >= margin 为 False
    ("  \n  \n  ", "  \n  \n  "),
    # 条件分支测试：line and len(line) >= margin 为 True
    ("  abc\n  def", "abc\ndef"),
    # 循环测试：空集合
    ("", ""),
    # 循环测试：单元素
    ("  abc", "abc"),
    # 循环测试：多元素
    ("  a\n  b\n  c", "a\nb\nc"),
    # 异常情况：非字符串输入
    (123, 123),
    # 异常情况：None输入
    (None, None),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected