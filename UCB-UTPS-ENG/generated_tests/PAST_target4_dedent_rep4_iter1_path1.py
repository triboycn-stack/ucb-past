# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None or indent < margin)
# 重复次数: 4, 迭代: 1
# 生成时间: 2026-04-26 06:24:53

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 情况1: 无非空行，返回原文本
    ("   \n   \n   ", "   \n   \n   "),
    # 情况2: 所有行都是空行，返回原文本
    ("   \n   \n   ", "   \n   \n   "),
    # 情况3: 有非空行，找到最小缩进
    ("  hello\n    world\n  goodbye", "hello\nworld\ngoodbye"),
    # 情况4: 有不同缩进的非空行
    ("   a\n  b\n c", "a\nb\nc"),
    # 情况5: 有空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 情况6: 首行是空行
    ("   \n  a\n  b", "a\nb"),
    # 情况7: 所有行缩进相同
    ("  a\n  b\n  c", "a\nb\nc"),
    # 情况8: 空字符串
    ("", ""),
    # 情况9: 单个非空行
    ("   hello", "hello"),
    # 情况10: 单个空行
    ("   \n", "   \n"),
    # 情况11: 多个空行和非空行
    ("   \n   \n  a\n   \n  b", "a\n\nb"),
    # 情况12: 边界情况：最大缩进
    ("                    a\n                    b", "a\nb"),
    # 情况13: 边界情况：最小缩进
    ("a\nb\nc", "a\nb\nc"),
    # 情况14: 非法输入（非字符串）
    (123, 123),
    # 情况15: 非法输入（None）
    (None, None),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected