# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None or indent < margin)
# 重复次数: 2, 迭代: 1
# 生成时间: 2026-04-26 06:22:38

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\nworld"),
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
    ("  hello", "hello"),
    # 多行不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    # 边界情况：margin为0
    ("hello\n  world", "hello\n  world"),
    # 边界情况：margin为最大值
    ("          a\n          b", "a\nb"),
    # 非空行在中间
    ("   \n  a\n   b", "  a\n   b"),
    # 非空行在末尾
    ("   \n   \n  a", "   \n   \na"),
    # 含有制表符
    ("\t\thello\n\t\tworld", "hello\nworld"),
    # 含有混合空格和制表符
    ("  \t  a\n  \t  b", "a\nb"),
    # 非法输入（非字符串）
    (123, TypeError),
    # 非法输入（None）
    (None, TypeError),
])
def test_dedent(text, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            dedent(text)
    else:
        result = dedent(text)
        assert result == expected