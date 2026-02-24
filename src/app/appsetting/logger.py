import logging
import logging as log
import sys
import uuid
from logging import basicConfig
from logging.handlers import RotatingFileHandler

"""Logger class that implements 2 handlers (file and stream)"""
class Logger:
    SESSION_ID = str(uuid.uuid4())[:8]
    # basicConfig(level=log.DEBUG, filename="log.log", filemode="w",
    #             format="%(asctime)s - %(levelname)s - %(message)s")

    # Specific logger for my app (named)
    _logger = log.getLogger("server_metrics")
    _logger.setLevel(log.DEBUG)
    if not _logger.handlers:
        fileformatter = log.Formatter(f"[Session: {SESSION_ID}] %(asctime)s - %(levelname)s - %(message)s")
        stream_formatter = fileformatter
        """File handler"""
        file_handler = RotatingFileHandler("log.log", maxBytes=5*1024*1024, backupCount=5, encoding="utf-8", mode="a")
        file_handler.setFormatter(fileformatter)
        _logger.addHandler(file_handler)

        """Console handler"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(fileformatter)
        _logger.addHandler(console_handler)

        """Session separators"""
        _logger.info("="*60)
        _logger.info(f"NEW SESSION STARTED | ID: {SESSION_ID}")
        _logger.info("="*60)

    """Static methods"""
    @classmethod
    def debug(cls, message):
        cls._logger.debug(msg=message)
    @classmethod
    def info(cls, message):
        cls._logger.info(msg=message)
    @classmethod
    def warning(cls, message):
        cls._logger.warning(msg=message)
    @classmethod
    def error(cls, message):
        cls._logger.error(exc_info=True, msg=message)
    @classmethod
    def critical(cls, message):
        cls._logger.critical(exc_info=True, msg=message)

