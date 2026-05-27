# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None
# 重复次数: 2, 迭代: 4
# 生成时间: 2026-04-26 06:23:01

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 条件分支测试: margin is None (所有行都是空行)
    ("", ""),
    ("\n\n", "\n\n"),
    ("   \n  \n   ", "   \n  \n   "),
    # 条件分支测试: margin is not None (存在非空行)
    ("  hello\n    world", "hello\n  world"),
    ("   a\n  b\n c", "a\nb\nc"),
    ("abc\n  def\n   ghi", "abc\ndef\nghi"),
    # 空集合测试: 没有非空行
    ("   \n  \n   ", "   \n  \n   "),
    # 单元素集合测试: 一个非空行
    ("  test", "test"),
    # 多元素集合测试: 多个非空行
    ("  line1\n  line2\n  line3", "line1\nline2\nline3"),
    # 边界条件测试: 最小缩进
    ("    a\n    b", "a\nb"),
    # 边界条件测试: 最大缩进
    ("a\nb", "a\nb"),
    # 边界条件测试: 临界值 (margin = len(line))
    ("  abc", "abc"),
    # 异常情况测试: 非字符串输入
    (123, 123),
    (None, None),
    # 异常情况测试: 无换行符
    ("  single line", "single line"),
    # 异常情况测试: 混合空行和非空行
    ("   \n  abc\n   \n def", "abc\n def"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected