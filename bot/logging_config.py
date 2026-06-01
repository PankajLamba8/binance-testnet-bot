import logging

def setup_logger():
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)
    
    # Create file handler
    fh = logging.FileHandler('bot_activity.log')
    fh.setLevel(logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # Add handler to logger
    if not logger.handlers:
        logger.addHandler(fh)
        
    return logger

logger = setup_logger()