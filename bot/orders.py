from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.client import get_binance_client
from bot.validators import validate_order_input
from bot.logging_config import logger

client = get_binance_client()

def place_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None, stop_price: float = None):
    try:
        # Validate inputs before sending to API
        symbol, side, order_type = validate_order_input(symbol, side, order_type, quantity, price, stop_price)
        
        logger.info(f"Attempting to place {order_type} {side} order for {quantity} {symbol}.")
        
        order_params = {
            'symbol': symbol,
            'side': side,
            'type': order_type,
            'quantity': quantity
        }
        
        if order_type == 'LIMIT':
            order_params['timeInForce'] = 'GTC' # Good Till Cancelled
            order_params['price'] = price
        elif order_type == 'STOP_MARKET':
            order_params['stopPrice'] = stop_price
            
        # Execute on Futures testnet
        response = client.futures_create_order(**order_params)
        logger.info(f"Order successful. Details: {response}")
        return response
        
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.status_code} - {e.message}")
        raise
    except BinanceRequestException as e:
        logger.error(f"Network Error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise