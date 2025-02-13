# tests/test_config_manager.py
import unittest
import json
import yaml
import os
from neurokit.config.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.json_config = {"test": "json"}
        self.yaml_config = {"test": "yaml"}
        with open("test_config.json", "w") as f:
            json.dump(self.json_config, f)
        with open("test_config.yaml", "w") as f:
            yaml.dump(self.yaml_config, f)
    
    def tearDown(self):
        if os.path.exists("test_config.json"):
            os.remove("test_config.json")
        if os.path.exists("test_config.yaml"):
            os.remove("test_config.yaml")
    
    def test_load_json_config(self):
        cm = ConfigManager("test_config.json")
        config = cm.load_config()
        self.assertEqual(config, self.json_config)
    
    def test_load_yaml_config(self):
        cm = ConfigManager("test_config.yaml")
        config = cm.load_config()
        self.assertEqual(config, self.yaml_config)

if __name__ == '__main__':
    unittest.main()
