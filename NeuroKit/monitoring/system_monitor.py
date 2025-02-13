# neurokit/monitoring/system_monitor.py
import psutil
import torch
import logging
from typing import Dict

logger = logging.getLogger("NeuroKit")

def get_memory_usage() -> Dict[str, float]:
    """
    Returns memory usage metrics.
    """
    mem = psutil.virtual_memory()
    return {
        "total": mem.total / (1024 ** 3),
        "available": mem.available / (1024 ** 3),
        "used": mem.used / (1024 ** 3),
        "percent": mem.percent
    }

def get_gpu_usage() -> Dict[str, float]:
    """
    Returns GPU usage metrics.
    """
    if not torch.cuda.is_available():
        return {}
    gpu_usage = {}
    try:
        for i in range(torch.cuda.device_count()):
            props = torch.cuda.get_device_properties(i)
            gpu_usage[f"gpu_{i}"] = {
                "name": props.name,
                "total_memory": props.total_memory / (1024 ** 3)
            }
    except Exception as e:
        logger.exception("Error retrieving GPU usage: %s", e)
    return gpu_usage

def get_temperature() -> Dict[str, float]:
    """
    Returns system temperature metrics, if available.
    """
    temps = {}
    try:
        sensor = psutil.sensors_temperatures()
        for name, entries in sensor.items():
            temps[name] = max(entry.current for entry in entries)
    except Exception as e:
        logger.warning("Temperature monitoring not available: %s", e)
    return temps

def run_diagnostics() -> None:
    """
    Runs a diagnostic report of system resources.
    """
    mem_usage = get_memory_usage()
    gpu_usage = get_gpu_usage()
    temperatures = get_temperature()
    logger.info("Memory Usage: %s", mem_usage)
    logger.info("GPU Usage: %s", gpu_usage)
    logger.info("Temperatures: %s", temperatures)
