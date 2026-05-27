# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: content
# 重复次数: 1, 迭代: 6
# 生成时间: 2026-05-23 09:00:44

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 空字符串
    ("", ""),
    # 单行无空格
    ("hello", "hello"),
    # 单行有空格
    ("  hello", "hello"),
    # 多行不同缩进
    ("  hello\n    world", "hello\nworld"),
    # 所有行都是空行
    ("\n\n", "\n\n"),
    # 有空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 首行为空
    ("  \n  a", "a"),
    # 所有行都有相同缩进
    ("  a\n  b\n  c", "a\nb\nc"),
    # 混合空行和非空行
    ("  a\n\n  b\n  c", "a\n\nb\nc"),
    # 边界情况：最大缩进
    ("        a", "a"),
    # 异常输入：非字符串
    (123, "123"),
    # 异常输入：None
    (None, "None"),
    # 异常输入：包含特殊字符
    ("  !@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`", "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected