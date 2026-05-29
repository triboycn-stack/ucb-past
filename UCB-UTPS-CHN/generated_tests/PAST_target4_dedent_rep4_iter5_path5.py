# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None)
# 重复次数: 4, 迭代: 5
# 生成时间: 2026-04-26 06:25:24

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\nworld"),
    # 带有空行的情况
    ("  a\n\n  b", "a\n\nb"),
    # 所有行都是空行
    ("\n\n", "\n\n"),
    # 无缩进的文本
    ("hello\nworld", "hello\nworld"),
    # 首行为空，其他行有缩进
    ("  \n  a\n  b", "  \na\nb"),
    # 多行不同缩进
    ("   a\n  b\n c", "a\nb\nc"),
    # 空字符串
    ("", ""),
    # 单行文本
    ("  test", "test"),
    # 多行文本，部分行无缩进
    ("  a\nb\n  c", "a\nb\nc"),
    # 混合空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 全部是空行
    ("   \n  \n ", "   \n  \n "),
    # 边界情况：最小缩进（0）
    ("a\nb", "a\nb"),
    # 边界情况：最大缩进（整行都是空格）
    ("      \n   abc", "      \nabc"),
    # 含有特殊字符
    ("  !@#$%^&*\n  abc123", "!@#$%^&*\nabc123"),
    # 非法输入：非字符串类型（虽然函数不处理，但测试是否抛出异常）
    (123, TypeError),
    # 非法输入：None
    (None, TypeError),
])
def test_dedent(text, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            dedent(text)
    else:
        result = dedent(text)
        assert result == expected