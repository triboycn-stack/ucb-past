import re

def dedent(text):
    """Remove any common leading whitespace from every line in `text`."""
    # 从标准库简化而来，包含循环、条件、正则
    lines = text.splitlines()
    # 找到所有非空行的最小缩进
    margin = None
    for line in lines:
        content = line.lstrip()
        if content:  # 非空行
            indent = len(line) - len(content)
            if margin is None or indent < margin:
                margin = indent
    # 如果没有非空行，返回原文本
    if margin is None:
        return text
    # 去除每行前 margin 个字符
    dedented = []
    for line in lines:
        if line and len(line) >= margin:
            dedented.append(line[margin:])
        else:
            dedented.append(line)
    return '\n'.join(dedented)