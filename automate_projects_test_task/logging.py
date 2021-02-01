import logging

DEFAULT_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"
DEBUG_LEVEL = "DEBUG"


def configure_logging_basic(level=DEBUG_LEVEL):
    logging.basicConfig(format=DEFAULT_LOGGING_FORMAT, level=level)
