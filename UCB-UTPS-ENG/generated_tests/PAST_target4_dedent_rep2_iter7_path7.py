# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (content)
# 重复次数: 2, 迭代: 7
# 生成时间: 2026-04-26 06:23:22

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 测试没有非空行的情况
    ("", ""),
    ("   \n   \n   ", "   \n   \n   "),
    # 测试所有行都是空行的情况
    ("   \n   \n   ", "   \n   \n   "),
    # 测试有非空行，但所有行缩进相同
    ("  hello\n  world", "hello\nworld"),
    # 测试有非空行，缩进不同
    ("  hello\n    world", "hello\n  world"),
    # 测试有非空行，缩进不同且有空行
    ("  hello\n\n    world", "hello\n\n  world"),
    # 测试有非空行，缩进不同且有前导空格的空行
    ("  \n  hello\n    world", "  \nhello\n  world"),
    # 测试边界情况：最小缩进（0）
    ("hello\nworld", "hello\nworld"),
    # 测试边界情况：最大缩进（超过行长度）
    ("   abc\ndef", "abc\ndef"),
    # 测试非法输入（非字符串）
    (123, TypeError),
    (None, TypeError),
    # 测试条件分支：content 为 False 的情况（空行）
    ("   \n  abc\n   ", "   \nabc\n   "),
    # 测试循环：空集合（无行）
    ("", ""),
    # 测试循环：单元素
    ("  abc", "abc"),
    # 测试循环：多元素
    ("  a\n  b\n  c", "a\nb\nc"),
    # 测试条件分支：margin 为 None 的情况（无非空行）
    ("   \n   \n   ", "   \n   \n   "),
])
def test_dedent(text, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            dedent(text)
    else:
        result = dedent(text)
        assert result == expected