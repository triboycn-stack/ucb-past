def scanstring(s, end, strict=True):
    """扫描 JSON 字符串，返回 (字符串值, 下一个索引) 或抛出 ValueError"""
    # 简化自 json.decoder.scanstring
    parts = []
    begin = end
    while True:
        try:
            ch = s[end]
        except IndexError:
            raise ValueError("Unterminated string")
        if ch == '"':
            break
        if ch == '\\':
            # 转义处理
            end += 1
            try:
                esc = s[end]
            except IndexError:
                raise ValueError("Unterminated string")
            if esc == '"':
                parts.append(s[begin:end-1] + '"')
                begin = end + 1
            elif esc == '\\':
                parts.append(s[begin:end-1] + '\\')
                begin = end + 1
            # ... 省略其他转义字符，保留主要逻辑
            else:
                raise ValueError("Invalid escape")
            end += 1
        else:
            end += 1
    parts.append(s[begin:end])
    return ''.join(parts), end + 1