# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None or indent < margin)
# 重复次数: 0, 迭代: 1
# 生成时间: 2026-05-23 08:59:12

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\nworld"),
    # 带有不同缩进的多行
    ("   a\n  b\n c", "a\nb\nc"),
    # 所有行都是空行
    ("\n\n\n", "\n\n\n"),
    # 混合空行和非空行
    ("   a\n\n   b", "a\n\nb"),
    # 无任何缩进
    ("hello\nworld", "hello\nworld"),
    # 首行为空
    ("\n  hello\n  world", "hello\nworld"),
    # 多个空行在中间
    ("  a\n\n  b\n  c", "a\n\nb\nc"),
    # 空字符串
    ("", ""),
    # 只有空行
    ("   \n   \n   ", "   \n   \n   "),
    # 一行非空，其他为空
    ("  abc\n\n   ", "abc\n\n   "),
    # 边界情况：最大缩进
    ("        a\n        b", "a\nb"),
    # 单行文本
    ("  test", "test"),
    # 单行空行
    ("   ", "   "),
    # 仅有一个非空行
    ("   line", "line"),
    # 非空行但没有缩进
    ("line\nanother", "line\nanother"),
    # 非空行但缩进不一致
    ("  a\n b\n  c", "a\nb\nc"),
    # 非空行但缩进为0
    ("a\nb\nc", "a\nb\nc"),
    # 非空行但缩进为1
    (" a\n b\n c", "a\nb\nc"),
    # 非空行但缩进为2
    ("  a\n  b\n  c", "a\nb\nc"),
    # 非空行但缩进为3
    ("   a\n   b\n   c", "a\nb\nc"),
    # 非空行但缩进为4
    ("    a\n    b\n    c", "a\nb\nc"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected