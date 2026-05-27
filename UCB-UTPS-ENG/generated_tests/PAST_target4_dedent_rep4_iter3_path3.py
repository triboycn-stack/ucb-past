# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (line and len(line) >= margin)
# 重复次数: 4, 迭代: 3
# 生成时间: 2026-04-26 06:25:06

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本用例
    ("  hello\n    world", "hello\nworld"),
    ("   a\n  b\nc", "a\nb\nc"),
    # 空行处理
    ("  \n  \n  ", "\n\n"),
    # 没有非空行的情况
    ("   \n   \n   ", "   \n   \n   "),
    # 边界情况：margin为0
    ("hello\nworld", "hello\nworld"),
    # 边界情况：margin为最大值
    ("    a\n    b", "a\nb"),
    # 条件分支测试：line and len(line) >= margin 为 False
    ("   \n  \n ", "\n\n "),
    # 循环测试：空集合
    ("", ""),
    # 循环测试：单元素
    ("  line", "line"),
    # 循环测试：多元素
    ("  a\n  b\n  c", "a\nb\nc"),
    # 异常情况：非字符串输入（虽然函数不处理，但应避免崩溃）
    (123, 123),
    # 特殊字符
    ("  !@#$\n  %^&*", "!@#$\n%^&*"),
    # 多种缩进混合
    ("   a\n  b\n c\n  d", "a\nb\nc\nd"),
])
def test_dedent(text, expected):
    result = dedent(text)
    assert result == expected