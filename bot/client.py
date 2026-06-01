import os
from dotenv import load_dotenv
from binance.client import Client
from bot.logging_config import logger

load_dotenv()

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    if not api_key or not api_secret:
        logger.error("API credentials missing in .env file.")
        raise ValueError("Please set BINANCE_API_KEY and BINANCE_API_SECRET in the .env file.")
    
    logger.info("Initializing Binance Futures Testnet client.")
    # testnet=True automatically routes to the testnet URLs
    return Client(api_key, api_secret, testnet=True)