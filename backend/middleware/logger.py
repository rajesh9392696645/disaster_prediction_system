# middleware/logger.py

import logging
import os
from datetime import datetime


class Logger:

    def __init__(self):

        # Create logs directory
        if not os.path.exists("logs"):

            os.makedirs("logs")

        # Log filename
        log_filename = (
            f"logs/system_"
            f"{datetime.now().strftime('%Y-%m-%d')}.log"
        )

        # Configure logger
        logging.basicConfig(

            level=logging.INFO,

            format=(
                "%(asctime)s - "
                "%(levelname)s - "
                "%(message)s"
            ),

            handlers=[

                logging.FileHandler(log_filename),

                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger(
            "AI_Disaster_System"
        )

    def info(self, message):

        self.logger.info(message)

    def warning(self, message):

        self.logger.warning(message)

    def error(self, message):

        self.logger.error(message)

    def critical(self, message):

        self.logger.critical(message)


# Initialize Logger
system_logger = Logger()