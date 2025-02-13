# neurokit/utils/env.py
import torch
import logging
import os

logger = logging.getLogger("NeuroKit")

def get_env_variable(var_name: str, default: str = "") -> str:
    """
    Retrieves an environment variable.
    """
    return os.getenv(var_name, default)

def cleanup_gpu_memory() -> None:
    """
    Cleans up GPU memory.
    """
    try:
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            logger.info("GPU memory cleaned up successfully.")
    except Exception as e:
        logger.exception("Error during GPU memory cleanup: %s", e)
