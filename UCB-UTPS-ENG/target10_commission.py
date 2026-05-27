def calculate_commission(locks: int, stocks: int, barrels: int) -> float:
    """
    计算销售人员的佣金

    销售规则：
    - 锁单价：$45
    - 股票单价：$30
    - 枪管单价：$25

    佣金计算规则：
    - 销售额 ≤ $1000: 佣金 = 销售额 × 10%
    - 销售额 ≤ $1800: 佣金 = 100 + (销售额-1000) × 15%
    - 销售额 > $1800: 佣金 = 220 + (销售额-1800) × 20%

    Args:
        locks: 锁销售数量（整数，≥0）
        stocks: 股票销售数量（整数，≥0）
        barrels: 枪管销售数量（整数，≥0）

    Returns:
        float: 计算的佣金金额
        输入无效时返回 -1.0
    """
    # 输入验证
    if not isinstance(locks, int) or not isinstance(stocks, int) or not isinstance(barrels, int):
        return -1.0

    if locks < 0 or stocks < 0 or barrels < 0:
        return -1.0

    # 计算销售额
    LOCK_PRICE = 45.0
    STOCK_PRICE = 30.0
    BARREL_PRICE = 25.0

    sales = locks * LOCK_PRICE + stocks * STOCK_PRICE + barrels * BARREL_PRICE

    # 边界检查（防止溢出）
    if sales < 0:
        return -1.0

    # 计算佣金
    if sales <= 1000:
        commission = sales * 0.10
    elif sales <= 1800:
        commission = 100 + (sales - 1000) * 0.15
    else:
        commission = 220 + (sales - 1800) * 0.20

    # 保留两位小数
    return round(commission, 2)