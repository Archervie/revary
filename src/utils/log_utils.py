import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


class Logger:
    """
    Handle all logging operations
    """

    def __init__(self) -> None:
        pass

    def create_log(self) -> Path:
        """
        Create the logging file

        Returns:
            Path: The path of the log file
        """
        log_dir = Path("data/logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        return log_dir / "revary.log"

    def logger(self, name: str) -> logging.Logger:
        """
        Apply the logging configuration with a specific name

        Args:
            name (str): The name of the module

        Returns:
            Logger: The specific Logger instance with the given name
        """
        return logging.getLogger(name)
