# 方法: PAST
# 目标文件: target4_dedent.py
# 条件路径: content
# 重复次数: 3, 迭代: 6
# 生成时间: 2026-04-26 06:24:26

import pytest
from target4_dedent import dedent

@pytest.mark.parametrize("text, expected", [
    # 基本情况：有非空行，正常去缩进
    ("  hello\n    world", "hello\nworld"),
    # 所有行都是空行
    ("\n\n\n", "\n\n\n"),
    # 混合空行和非空行
    ("  a\n\n  b", "a\n\nb"),
    # 首行是空行，其他行有内容
    ("\n  hello\n  world", "hello\nworld"),
    # 所有行都为空，但有换行符
    ("   \n   \n   ", "   \n   \n   "),
    # 空字符串
    ("", ""),
    # 单行无缩进
    ("hello", "hello"),
    # 单行有缩进
    ("   hello", "hello"),
    # 多行不同缩进
    ("  a\n   b\n    c", "a\nb\nc"),
    # 边界情况：最大缩进
    ("        a\n        b", "a\nb"),
    # 异常输入：非字符串类型（虽然函数不处理，但测试是否抛出异常）
    (12345, TypeError),
    # 异常输入：None
    (None, TypeError),
    # 仅包含空行
    ("   \n   \n   ", "   \n   \n   "),
    # 有前导空格的空行
    ("   \n  abc", "  abc"),
    # 有后缀空格的行
    ("  abc  ", "abc  "),
    # 混合空行和非空行，且有不同缩进
    ("  a\n\n   b\n  c", "a\n\nb\nc"),
])
def test_dedent(text, expected):
    if isinstance(expected, type) and expected is TypeError:
        with pytest.raises(TypeError):
            dedent(text)
    else:
        result = dedent(text)
        assert result == expected