"""Setup some basic console and file logging."""
import logging
import os

from src.config import LOGS_DIR
from src.utils import get_timestamp


def setup_logging():
    """Configure logging for the whole program."""
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # set custom levels for third party modules, so we don't get spammed with debug messages
    custom_log_levels = {
        "matplotlib": logging.INFO,
    }

    for logger_name, custom_level in custom_log_levels.items():
        logging.getLogger(logger_name).setLevel(custom_level)

    # this log format produces, e.g.
    # 2020-01-01 12:00:00,000 - my_module - DEBUG  - hello world
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # configure the console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(fmt)
    root_logger.addHandler(console_handler)

    # configure the file handler
    log_filename = "log_{}.log".format(get_timestamp())
    file_handler = logging.FileHandler(os.path.join(LOGS_DIR, log_filename))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(fmt)
    root_logger.addHandler(file_handler)

    # now the root_logger has been configured
    # # we can nicely access it with logging.getLogger(__name__)
