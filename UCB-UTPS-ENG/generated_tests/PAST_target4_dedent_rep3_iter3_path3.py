# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (line and len(line) >= margin)
# 重复次数: 3, 迭代: 3
# 生成时间: 2026-04-26 06:23:59

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\nworld"),
    ("   a\n  b\nc", "a\nb\nc"),
    # 空行处理
    ("\n  a\n\n  b", "\n a\n\n b"),
    # 所有行都是空行
    ("   \n  \n ", "   \n  \n "),
    # 没有非空行
    ("   \n  \n   ", "   \n  \n   "),
    # 边界情况：margin为0
    ("hello\nworld", "hello\nworld"),
    # 边界情况：margin为最大值
    ("        abc", "abc"),
    # 条件分支测试: line and len(line) >= margin 为 False
    ("   \n  \n   ", "   \n  \n   "),
    # 条件分支测试: line and len(line) >= margin 为 True
    ("   abc\n  def", "abc\ndef"),
    # 多元素循环测试
    ("  a\n  b\n  c", "a\nb\nc"),
    # 单元素循环测试
    ("  a", "a"),
    # 空集合（无非空行）
    ("   \n  \n   ", "   \n  \n   "),
    # 非法输入
    (None, None),
    (123, 123),
    (["  a", "  b"], ["  a", "  b"]),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected