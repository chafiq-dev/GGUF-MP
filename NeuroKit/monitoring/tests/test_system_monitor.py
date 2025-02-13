# tests/test_system_monitor.py
import unittest
from neurokit.monitoring.system_monitor import get_memory_usage, get_gpu_usage, get_temperature

class TestSystemMonitor(unittest.TestCase):
    def test_memory_usage(self):
        mem_usage = get_memory_usage()
        self.assertIn("total", mem_usage)
    
    def test_gpu_usage(self):
        gpu_usage = get_gpu_usage()
        self.assertIsInstance(gpu_usage, dict)
    
    def test_temperature(self):
        temps = get_temperature()
        self.assertIsInstance(temps, dict)

if __name__ == '__main__':
    unittest.main()
