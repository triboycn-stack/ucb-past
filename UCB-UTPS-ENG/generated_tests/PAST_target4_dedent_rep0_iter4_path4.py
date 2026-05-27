# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: margin is None
# 重复次数: 0, 迭代: 4
# 生成时间: 2026-05-23 08:59:33

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 情况1: 所有行都是空行，margin为None
    ("   \n  \n ", "   \n  \n "),
    # 情况2: 有非空行，计算正确缩进
    ("  hello\n    world", "hello\n  world"),
    # 情况3: 非空行前有不同缩进
    ("   a\n  b\n c", "a\nb\nc"),
    # 情况4: 首行为空，其他行有内容
    ("\n   abc\n  def", "abc\ndef"),
    # 情况5: 多行，其中某行为空
    ("  a\n\n  b", "a\n\nb"),
    # 情况6: 空字符串
    ("", ""),
    # 情况7: 单行非空
    ("   test", "test"),
    # 情况8: 单行空
    ("   ", "   "),
    # 情况9: 多行，所有行缩进相同
    ("  a\n  b\n  c", "a\nb\nc"),
    # 情况10: 有换行符但无内容
    ("  \n  \n  ", "  \n  \n  "),
    # 情况11: 有特殊字符
    ("  !@#$\n  %^&*", "!@#$\n%&*"),
    # 情况12: 包含制表符
    ("\t\ttab\n\t\tline", "tab\nline"),
    # 情况13: 有混合空格和制表符
    ("  \t  mixed\n  \t  content", "mixed\ncontent"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected