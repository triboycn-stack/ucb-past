# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None or indent < margin)
# 重复次数: 3, 迭代: 1
# 生成时间: 2026-04-26 06:23:43

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 情况1: 无非空行，返回原文本
    ("   \n   \n   ", "   \n   \n   "),
    # 情况2: 所有行都是空行，返回原文本
    ("   \n   \n   ", "   \n   \n   "),
    # 情况3: 有非空行，找到最小缩进
    ("  hello\n    world\n  goodbye", "hello\n  world\ngoodbye"),
    # 情况4: 非空行缩进不同，取最小值
    ("   a\n  b\n c", "a\nb\nc"),
    # 情况5: 非空行缩进相同
    ("  a\n  b\n  c", "a\nb\nc"),
    # 情况6: 有空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 情况7: 有前导空格但没有非空行
    ("   \n  \n   ", "   \n  \n   "),
    # 情况8: 空字符串
    ("", ""),
    # 情况9: 单行非空
    ("  hello", "hello"),
    # 情况10: 单行空行
    ("   ", "   "),
    # 情况11: 多行非空，缩进不同
    ("   a\n  b\n c\n  d", "a\nb\nc\nd"),
    # 情况12: 边界条件：最大缩进
    (" " * 100 + "hello", "hello"),
    # 情况13: 边界条件：最小缩进（0）
    ("hello\n  world", "hello\n  world"),
    # 情况14: 异常输入：非字符串
    (123, 123),
    # 情况15: 异常输入：None
    (None, None),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected