import os
import logging
from config import LOG_DIR, LOG_FILE_PATH

def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(LOG_FILE_PATH, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )