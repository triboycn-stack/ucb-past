# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: content
# 重复次数: 2, 迭代: 6
# 生成时间: 2026-04-26 06:23:15

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\nworld"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc", "  \nabc"),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行
    ("   \n   \n   ", "   \n   \n   "),
    # 非空行的最小缩进为0
    ("hello\n  world", "hello\n  world"),
    # 非空行的最小缩进为2
    ("  hello\n  world", "hello\nworld"),
    # 单行文本
    ("  test", "test"),
    # 多行文本，部分行为空
    ("  a\n\n  b", "a\n\nb"),
    # 边界情况：空字符串
    ("", ""),
    # 边界情况：仅空行
    ("   \n   ", "   \n   "),
    # 异常情况：非字符串输入（虽然函数不处理，但应避免崩溃）
    (123, 123),
    # 异常情况：None输入
    (None, None),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected