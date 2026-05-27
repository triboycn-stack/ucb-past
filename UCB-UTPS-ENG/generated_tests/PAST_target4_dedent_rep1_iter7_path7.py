# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (content)
# 重复次数: 1, 迭代: 7
# 生成时间: 2026-05-23 09:00:50

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\nworld"),
    # 所有行都是空行
    ("\n\n\n", "\n\n\n"),
    # 混合空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 首行为空，其他行有缩进
    ("  \n  abc\n  def", "abc\ndef"),
    # 没有非空行（所有行都为空）
    ("   \n   \n   ", "   \n   \n   "),
    # 空字符串
    ("", ""),
    # 单行无缩进
    ("hello", "hello"),
    # 单行有缩进
    ("   hello", "hello"),
    # 多行不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    # 行尾有空格
    ("  hello  \n  world  ", "hello  \nworld  "),
    # 包含制表符
    ("\t\thello\n\t\tworld", "hello\nworld"),
    # 边界情况：最大缩进
    ("                    a\n                    b", "a\nb"),
    # 边界情况：最小缩进（0）
    ("a\nb", "a\nb"),
    # 非法输入：非字符串类型
    (12345, 12345),
    # 非法输入：None
    (None, None),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected