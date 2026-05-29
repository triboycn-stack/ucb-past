# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None
# 重复次数: 4, 迭代: 4
# 生成时间: 2026-04-26 06:25:14

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 条件分支：margin is None（所有行都是空行）
    ("", ""),
    ("\n\n", "\n\n"),
    ("   \n  \n ", "   \n  \n "),
    # 条件分支：margin is not None（存在非空行）
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    ("  line1\n  line2\n  line3", "line1\nline2\nline3"),
    # 空集合（无行）
    ("", ""),
    # 单元素情况
    ("  single", "single"),
    # 多元素情况
    ("  line1\n  line2\n  line3", "line1\nline2\nline3"),
    # 边界条件：最小值（0个空格）
    ("no_indent\nanother_line", "no_indent\nanother_line"),
    # 边界条件：最大值（全为空格）
    ("         \n         ", "         \n         "),
    # 异常情况：非字符串输入（虽然函数接受任何可分割为行的对象，但此处测试字符串）
    (12345, "12345"),
    (None, "None"),
    # 混合空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 行首有多个空格，但内容相同
    ("   abc\n   abc\n   abc", "abc\nabc\nabc"),
    # 行首有不同缩进
    ("   abc\n  def\n ghi", "abc\ndef\nghi"),
    # 特殊字符和缩进
    ("  !@#$%^&*\n  abc123", "!@#$%^&*\nabc123"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected