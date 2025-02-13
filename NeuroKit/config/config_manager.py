# neurokit/config/config_manager.py
import json
import yaml
from typing import Any, Dict
from neurokit.utils.logger import logger

class ConfigManager:
    """
    Manages configuration loading from JSON or YAML files.
    """
    def __init__(self, config_path: str) -> None:
        self.config_path = config_path

    def load_config(self) -> Dict[str, Any]:
        """
        Loads configuration from a JSON or YAML file based on file extension.
        """
        try:
            if self.config_path.endswith('.json'):
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
            elif self.config_path.endswith(('.yml', '.yaml')):
                with open(self.config_path, 'r') as f:
                    config = yaml.safe_load(f)
            else:
                raise ValueError("Unsupported configuration file format.")
            logger.info("Configuration loaded successfully from %s", self.config_path)
            return config
        except Exception as e:
            logger.exception("Error loading configuration: %s", e)
            raise
