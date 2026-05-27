# target7_is_valid_js_identifier.py
import re

def is_valid_js_identifier(name: str) -> bool:
    if not name:
        return False
    if not re.match(r'^[a-zA-Z_$][a-zA-Z0-9_$]*$', name):
        return False
    reserved_keywords = {
        'break', 'case', 'catch', 'class', 'const', 'continue',
        'debugger', 'default', 'delete', 'do', 'else', 'export',
        'extends', 'finally', 'for', 'function', 'if', 'import',
        'in', 'instanceof', 'new', 'return', 'super', 'switch',
        'this', 'throw', 'try', 'typeof', 'var', 'void', 'while',
        'with', 'yield', 'let', 'static'
    }
    return name not in reserved_keywords