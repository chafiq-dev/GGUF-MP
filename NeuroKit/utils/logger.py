# neurokit/utils/logger.py
import logging
import sys

def setup_logging() -> None:
    """
    Configures the logging system.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

setup_logging()
logger = logging.getLogger("NeuroKit")
