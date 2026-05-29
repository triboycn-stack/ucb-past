# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (content)
# 重复次数: 3, 迭代: 7
# 生成时间: 2026-04-26 06:24:36

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    ("  abc\n  def\n  ghi", "abc\ndef\nghi"),
    # 空行处理
    ("  \n  \n  ", "\n\n"),
    # 没有非空行
    ("   \n   \n   ", "   \n   \n   "),
    # 单行情况
    ("   single line", "single line"),
    # 多行不同缩进
    ("   a\n  b\n c", "a\nb\nc"),
    # 首行为空
    ("\n  line1\n  line2", "\nline1\nline2"),
    # 尾行为空
    ("line1\nline2\n   ", "line1\nline2\n"),
    # 全部为空行
    ("   \n   \n   ", "   \n   \n   "),
    # 边界情况：空字符串
    ("", ""),
    # 边界情况：单个空行
    ("   \n", "   \n"),
    # 异常输入
    (None, None),
    (123, 123),
    # 条件分支测试（content为空）
    ("   \n  abc", "   \nabc"),
    ("   \n   \n  abc", "   \n   \nabc"),
    # 循环测试（空集合）
    ("", ""),
    # 循环测试（单元素）
    ("   test", "test"),
    # 循环测试（多元素）
    ("   a\n   b\n   c", "a\nb\nc"),
    # 边界条件：最大缩进
    (" " * 100 + "text", "text"),
    # 边界条件：临界值
    (" " * 10 + "text", "text"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected