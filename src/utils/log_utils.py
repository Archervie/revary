import logging


class Logger:
    def __init__(self) -> None:
        pass

    def logger(self, name) -> logging.Logger:
        return logging.getLogger(name)
