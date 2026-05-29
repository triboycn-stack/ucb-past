def classify_triangle(a: float, b: float, c: float) -> str:
    """
    判断三角形的类型

    Args:
        a, b, c: 三角形的三条边长

    Returns:
        str: "INVALID" - 无效三角形
             "EQUILATERAL" - 等边三角形
             "ISOSCELES" - 等腰三角形
             "SCALENE" - 不等边三角形
             "ERROR" - 输入错误
    """
    # 输入验证
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "ERROR"

    if a <= 0 or b <= 0 or c <= 0:
        return "INVALID"

    # 三角形不等式定理：任意两边之和大于第三边
    if a + b <= c or a + c <= b or b + c <= a:
        return "INVALID"

    # 三角形分类
    if a == b == c:
        return "EQUILATERAL"
    elif a == b or b == c or a == c:
        return "ISOSCELES"
    else:
        return "SCALENE"