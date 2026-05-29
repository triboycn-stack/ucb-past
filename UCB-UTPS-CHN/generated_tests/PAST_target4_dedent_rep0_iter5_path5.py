# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None)
# 重复次数: 0, 迭代: 5
# 生成时间: 2026-05-23 08:59:39

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\n  world"),
    # 多行，不同缩进
    ("   a\n  b\n c", "a\nb\nc"),
    # 首行为空
    ("\n  hello\n    world", "\nhello\n  world"),
    # 所有行都为空
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行
    ("   \n   \n   ", "   \n   \n   "),
    # 空字符串
    ("", ""),
    # 单行，无缩进
    ("hello", "hello"),
    # 单行，有缩进
    ("  hello", "hello"),
    # 混合空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 边界情况：最大缩进
    ("        a\n        b", "a\nb"),
    # 边界情况：最小缩进
    ("a\nb", "a\nb"),
    # 异常输入：非字符串
    (123, 123),
    # 异常输入：None
    (None, None),
])
def test_dedent_core_logic(text, expected):
    result = dedent(text)
    assert result == expected