# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (line and len(line) >= margin)
# 重复次数: 0, 迭代: 3
# 生成时间: 2026-05-23 08:59:27

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\nworld"),
    # 带有空行的情况
    ("  a\n\n  b", "a\n\nb"),
    # 所有行都是空行
    ("\n\n", "\n\n"),
    # 所有行都是空行，但有换行符
    ("   \n   \n   ", "   \n   \n   "),
    # 没有非空行，返回原文本
    ("   \n   \n   ", "   \n   \n   "),
    # 非空行的最小缩进为0
    ("hello\nworld", "hello\nworld"),
    # 非空行的最小缩进为2
    ("  hello\n  world", "hello\nworld"),
    # 行首有多个空格，但长度不足margin
    ("   abc\n  def", "abc\ndef"),
    # 行首有多个空格，长度刚好等于margin
    ("   abc\n   def", "abc\ndef"),
    # 行首有多个空格，长度超过margin
    ("     abc\n   def", "abc\ndef"),
    # 空字符串
    ("", ""),
    # 单行文本
    ("  test", "test"),
    # 多行文本，部分行为空
    ("  a\n\n  b\n  c", "a\n\nb\nc"),
    # 边界情况：margin为0
    ("a\n  b", "a\nb"),
    # 边界情况：margin为最大可能值（整行为空）
    ("   \n   \n   ", "   \n   \n   "),
    # 异常输入：非字符串类型
    (123, TypeError),
    # 异常输入：None
    (None, TypeError),
])
def test_dedent(text, expected):
    if isinstance(expected, type) and expected is TypeError:
        with pytest.raises(TypeError):
            dedent(text)
    else:
        result = dedent(text)
        assert result == expected