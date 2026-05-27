# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None
# 重复次数: 1, 迭代: 4
# 生成时间: 2026-05-23 09:00:31

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 情况1: 无非空行，margin is None
    ("   \n   \n   ", "   \n   \n   "),
    # 情况2: 有非空行，找到最小缩进
    ("  hello\n    world\n  goodbye", "hello\n  world\ngoodbye"),
    # 情况3: 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 情况4: 有混合空行和非空行
    ("  a\n\n  b\n  c", "a\n\nb\nc"),
    # 情况5: 仅有一行非空
    ("  line", "line"),
    # 情况6: 多行，不同缩进
    ("  abc\n   def\n  ghi", "abc\n def\nghi"),
    # 情况7: 空字符串
    ("", ""),
    # 情况8: 单个字符
    (" a", "a"),
    # 情况9: 有换行符但没有内容
    ("  \n  \n  ", "  \n  \n  "),
    # 情况10: 首行是空行，其他行有内容
    ("  \n  abc\n  def", "  \nabc\ndef"),
    # 情况11: 有多个空行
    ("   \n  \n   \n  abc", "   \n  \n   \nabc"),
    # 情况12: 边界情况：最大缩进
    ("        abc", "abc"),
    # 情况13: 非法输入（非字符串）
    (123, 123),
    # 情况14: 非法输入（None）
    (None, None),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected