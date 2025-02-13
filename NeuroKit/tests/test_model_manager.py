# tests/test_model_manager.py
import unittest
import os
import torch
from neurokit.core.model_manager import ModelManager

class TestModelManager(unittest.TestCase):
    def setUp(self):
        # Create a dummy model and save it for testing
        self.model = torch.nn.Linear(10, 2)
        self.test_model_path = "dummy_model.pth"
        torch.save(self.model, self.test_model_path)
    
    def tearDown(self):
        if os.path.exists(self.test_model_path):
            os.remove(self.test_model_path)
    
    def test_load_model(self):
        mm = ModelManager(model_path=self.test_model_path)
        loaded_model = mm.load_model()
        self.assertIsNotNone(loaded_model)
    
    def test_quantize_model_without_loading(self):
        mm = ModelManager(model_path=self.test_model_path)
        with self.assertRaises(ValueError):
            mm.quantize_model("8bit")

if __name__ == '__main__':
    unittest.main()
