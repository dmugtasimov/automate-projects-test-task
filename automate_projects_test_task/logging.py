import logging

DEFAULT_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(name)s %(message)s"
DEBUG_LEVEL = "DEBUG"


def configure_logging_basic(level: str = DEBUG_LEVEL) -> None:
    logging.basicConfig(format=DEFAULT_LOGGING_FORMAT, level=level)
