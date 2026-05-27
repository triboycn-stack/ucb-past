# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: not (margin is None)
# 重复次数: 3, 迭代: 5
# 生成时间: 2026-04-26 06:24:16

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，存在缩进
    ("  hello\n    world", "hello\nworld"),
    # 带有前导空格和空行
    ("  a\n\n  b", "a\n\nb"),
    # 所有行都是空行
    ("\n\n", "\n\n"),
    # 仅有一行，无缩进
    ("hello", "hello"),
    # 仅有一行，有缩进
    ("   hello", "hello"),
    # 多行，不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    # 空字符串
    ("", ""),
    # 仅含空行
    ("   \n   ", "   \n   "),
    # 混合空行和非空行
    ("  a\n\n  b\n  c", "a\n\nb\nc"),
    # 边界情况：最大可能的缩进
    (" " * 100 + "hello", "hello"),
    # 非法输入：非字符串类型（虽然函数不处理，但测试是否抛出异常）
    (123, TypeError),
    # 非法输入：None
    (None, TypeError),
])
def test_dedent(text, expected):
    if isinstance(expected, type) and expected is TypeError:
        with pytest.raises(TypeError):
            dedent(text)
    else:
        result = dedent(text)
        assert result == expected