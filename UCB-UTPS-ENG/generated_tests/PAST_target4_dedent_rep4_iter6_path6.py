# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: content
# 重复次数: 4, 迭代: 6
# 生成时间: 2026-04-26 06:25:30

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\n  world"),
    # 空行处理
    ("  \n  a\n  b", "\na\nb"),
    # 所有行都是空行
    ("   \n  \n ", "   \n  \n "),
    # 没有非空行
    ("   \n  \n   ", "   \n  \n   "),
    # 单行非空
    ("   abc", "abc"),
    # 多行不同缩进
    ("  a\n   b\n  c", "a\n b\nc"),
    # 首行为空
    ("\n  a\n  b", "\n a\n b"),
    # 行尾有空格
    ("  abc  \n  def  ", "abc  \ndef  "),
    # 边界情况：最小缩进
    ("a\n b", "a\nb"),
    # 边界情况：最大缩进（超过行长度）
    ("   abc", "abc"),
    # 异常输入
    (None, None),
    (123, 123),
    (["  a", "  b"], ["  a", "  b"]),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected