from logging import Logger, Formatter
from logging.handlers import TimedRotatingFileHandler
import os
from decouple import config

def create_log_directory():
    os.makedirs(os.getcwd() + "/Log")

def setup_logger():
    create_log_directory()
    log_file_path = os.getcwd() + "/Log/logs.log"

    file_handler = TimedRotatingFileHandler(
        filename=log_file_path,
        when="d", interval=1)
    
    log_formatter = Formatter(
        fmt="%(asctime)s-%(levelname)s: %(filename)s-%(funcName)s-%(lineno)d => %(message)s")
    file_handler.setFormatter(log_formatter)

    logger = Logger(name="raspberrypi_dashboard_project", level=config("log_level", cast=int))
    logger.handlers = []
    logger.addHandler(file_handler)
    return logger

log = setup_logger()