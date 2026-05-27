# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None or indent < margin)
# 重复次数: 1, 迭代: 1
# 生成时间: 2026-05-23 09:00:07

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\n  world"),
    # 带有空行的情况
    ("  a\n\n  b", "a\n\nb"),
    # 所有行都是空行
    ("\n\n", "\n\n"),
    # 没有非空行
    ("   \n   ", "   \n   "),
    # 空字符串
    ("", ""),
    # 单行无缩进
    ("hello", "hello"),
    # 单行有缩进
    ("   hello", "hello"),
    # 多行不同缩进
    ("  a\n   b\n    c", "a\n b\n  c"),
    # 边界情况：margin为0
    ("hello\n  world", "hello\n  world"),
    # 边界情况：margin为最大值（行长度）
    ("a\n  b", "a\n  b"),
    # 非法输入：非字符串类型
    (123, 123),
    # 非法输入：None
    (None, None),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected