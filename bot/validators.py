def validate_order_input(symbol: str, side: str, order_type: str, quantity: float, price: float = None, stop_price: float = None):
    valid_sides = ['BUY', 'SELL']
    valid_types = ['MARKET', 'LIMIT', 'STOP_MARKET']
    
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()
    
    if side not in valid_sides:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL.")
    if order_type not in valid_types:
        raise ValueError(f"Invalid order type: {order_type}. Must be MARKET, LIMIT, or STOP_MARKET.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    if order_type == 'LIMIT' and (price is None or price <= 0):
        raise ValueError("A valid price must be provided for LIMIT orders.")
    if order_type == 'STOP_MARKET' and (stop_price is None or stop_price <= 0):
        raise ValueError("A valid stop_price must be provided for STOP_MARKET orders.")
        
    return symbol, side, order_type