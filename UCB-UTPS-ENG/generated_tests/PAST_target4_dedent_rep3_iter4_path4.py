# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None
# 重复次数: 3, 迭代: 4
# 生成时间: 2026-04-26 06:24:08

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 情况1: 无非空行，margin is None
    ("   \n   \n   ", "   \n   \n   "),
    # 情况2: 所有行都是空行，margin is None
    ("   \n   \n   ", "   \n   \n   "),
    # 情况3: 有非空行，找到最小缩进
    ("  hello\n    world\n  goodbye", "hello\nworld\ngoodbye"),
    # 情况4: 有非空行，但缩进不同
    ("  a\n    b\n  c", "a\nb\nc"),
    # 情况5: 有非空行，但缩进相同
    ("  abc\n  def\n  ghi", "abc\ndef\nghi"),
    # 情况6: 空字符串
    ("", ""),
    # 情况7: 单行非空
    ("  hello", "hello"),
    # 情况8: 单行空行
    ("   ", "   "),
    # 情况9: 多行混合空行和非空行
    ("  a\n\n  b\n  c", "a\n\nb\nc"),
    # 情况10: 带有制表符的缩进
    ("\t\thello\n\t\tworld", "hello\nworld"),
    # 情况11: 不同类型的空白字符
    ("  \t  abc\n  \t  def", "abc\ndef"),
    # 情况12: 边界情况：最大缩进（超过行长度）
    ("        abc", "abc"),
    # 情况13: 非法输入（非字符串）
    (123, 123),
    # 情况14: 非法输入（None）
    (None, None),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected