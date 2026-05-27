# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (content)
# 重复次数: 0, 迭代: 7
# 生成时间: 2026-05-23 08:59:53

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    ("  abc\n  def\n  ghi", "abc\ndef\nghi"),
    # 空行处理
    ("  \n  \n  ", "\n\n "),
    # 没有非空行的情况
    ("   \n   \n   ", "   \n   \n   "),
    # 单行情况
    ("   test", "test"),
    # 多行但无缩进
    ("hello\nworld", "hello\nworld"),
    # 混合空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 边界情况：全空行
    ("   \n   \n   ", "   \n   \n   "),
    # 边界情况：单个空行
    ("   \n", "   \n"),
    # 异常输入
    (None, None),
    (123, 123),
    (["  a", "  b"], ["  a", "  b"]),
    # 条件分支测试：content为空的情况
    ("   \n  abc", "   \nabc"),
    # 循环测试：空集合
    ("", ""),
    # 循环测试：单元素
    ("  a", "a"),
    # 循环测试：多元素
    ("  a\n  b\n  c", "a\nb\nc"),
    # 边界条件：最大值（长字符串）
    (" " * 100 + "abc", "abc"),
    # 特殊字符
    ("  !@#$%^&*()\n  abc", "!@#$%^&*()\nabc"),
    # 缩进不一致
    ("  a\n   b\n  c", "a\n b\nc"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected