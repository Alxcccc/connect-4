import logging

class Connecta4Logging():
    def __init__(self):
        logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )
        
    def info(self, message: str):
        logging.info(message)
        
    def warning(self, message: str):
        logging.warning(message)
        
    def error(self, message: str):
        logging.error(message)
        
    def critical(self, message: str):
        logging.critical(message)