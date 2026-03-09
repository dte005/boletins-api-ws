import logging
import sys


def logging_setup(level: str) -> logging.Logger:
    logger = logging.getLogger("rpa")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logger.level)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
    return logger
