# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: line and len(line) >= margin
# 重复次数: 3, 迭代: 2
# 生成时间: 2026-04-26 06:23:53

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况
    ("  hello\n    world", "hello\n  world"),
    ("   a\n   b\n   c", "a\nb\nc"),
    # 空行处理
    ("  \n  abc\n  def", "  \nabc\ndef"),
    # 没有非空行
    ("   \n   ", "   \n   "),
    # 所有行都是空行
    ("   \n   \n   ", "   \n   \n   "),
    # 只有一行
    ("   test", "test"),
    # 行首有多个空格
    ("     line1\n     line2", "line1\nline2"),
    # 行首有不同缩进
    ("  line1\n   line2\n    line3", "line1\nline2\nline3"),
    # 边界情况：margin为0
    ("line1\nline2", "line1\nline2"),
    # 边界情况：margin为最大值
    ("          line1\n          line2", "line1\nline2"),
    # 非空行但没有前导空格
    ("line1\n  line2", "line1\n  line2"),
    # 非空行但前导空格不足
    (" line1\n  line2", "line1\n line2"),
    # 非空行但前导空格足够
    ("   line1\n   line2", "line1\nline2"),
    # 非空行但前导空格不足且有其他字符
    ("  a\n  b\nc", "a\nb\nc"),
    # 非空行但前导空格足够且有其他字符
    ("   a\n   b\nc", "a\nb\nc"),
    # 非空行但前导空格足够且有其他字符（多行）
    ("   a\n   b\n   c", "a\nb\nc"),
    # 非空行但前导空格足够且有其他字符（单行）
    ("   a", "a"),
    # 非空行但前导空格足够且有其他字符（多行，部分行无前导空格）
    ("   a\n   b\n c", "a\nb\n c"),
    # 非空行但前导空格足够且有其他字符（多行，部分行无前导空格）
    ("   a\n   b\n  c", "a\nb\n c"),
    # 非空行但前导空格足够且有其他字符（多行，部分行无前导空格）
    ("   a\n   b\n c", "a\nb\n c"),
    # 非空行但前导空格足够且有其他字符（多行，部分行无前导空格）
    ("   a\n   b\n  c", "a\nb\n c"),
    # 非空行但前导空格足够且有其他字符（多行，部分行无前导空格）
    ("   a\n   b\n c", "a\nb\n c"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected