import os
import sys
import logging

logging_str = "[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"
logDir = "logs"
logFilePath = os.path.join(logDir,"currentLog.log")
os.makedirs(logDir,exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(logFilePath),
        logging.StreamHandler(sys.stdout)
    ]
)

loggerInstance = logging.getLogger("textSummarizer")