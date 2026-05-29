# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None)
# 重复次数: 1, 迭代: 5
# 生成时间: 2026-05-23 09:00:38

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\nworld"),
    # 带有空行的情况
    ("  a\n\n  b", "a\n\nb"),
    # 所有行都是空行
    ("\n\n", "\n\n"),
    # 所有行都是空行，但有换行符
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行，返回原文本
    ("   \n   \n   ", "   \n   \n   "),
    # 单行非空
    ("  line", "line"),
    # 多行不同缩进
    ("  abc\n   def\n  ghi", "abc\ndef\nghi"),
    # 边界情况：最小缩进（0）
    ("abc\n def", "abc\n def"),
    # 边界情况：最大缩进（行长度）
    ("     ", "     "),
    # 非法输入：非字符串类型
    (123, 123),
    # 空字符串
    ("", ""),
    # 仅包含换行符
    ("\n\n", "\n\n"),
    # 混合空行和非空行
    ("  a\n\n  b\n  c", "a\n\nb\nc"),
    # 行首有多个空格，但内容为空
    ("   \n   \n   ", "   \n   \n   "),
    # 行首有制表符
    ("\t\thello\n\t\tworld", "hello\nworld"),
    # 混合空格和制表符
    ("  \t  hello\n  \t  world", "hello\nworld"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected