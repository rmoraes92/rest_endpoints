import logging
import sys


def setup_logger(log_level=logging.INFO, file_handler_path=None) -> logging.Logger:
    """
    Set up a logger that outputs to both stdout and a file named logs.txt

    Args:
        log_level: The logging level (default: logging.INFO)

    Returns:
        A configured logger instance
    """
    # Create logger
    logger = logging.getLogger("rest_endpoints")
    logger.setLevel(log_level)

    # Create formatter
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

    # Create file handler
    if file_handler_path:
        file_handler = logging.FileHandler(file_handler_path)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()
