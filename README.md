# NeuroKit

## Description
NeuroKit is a Python utility designed for managing and optimizing GGUF language models with advanced PyTorch integration. It intelligently handles model caching, quantization, gradient checkpointing, and system monitoring, ensuring seamless performance across both GPU and CPU environments. NeuroKit is engineered for production-grade reliability and extensive configurability.

## Features

- **Advanced PyTorch Integration:** Leverages CUDA support for GPU acceleration with automatic CPU fallback when GPUs are unavailable.
- **Intelligent Model Caching:** Caches models for fast reloads and improved performance.
- **Model Quantization:** Supports both 4-bit and 8-bit quantization to optimize memory usage.
- **Gradient Checkpointing:** Reduces memory footprint for large models.
- **Multiple Configuration Formats:** Accepts both JSON and YAML configuration files for flexible setup.
- **Comprehensive Error Handling & Recovery:** Robust error management throughout the tool.
- **Real-Time System Monitoring:** Tracks memory usage, GPU utilization, and system temperatures.
- **Performance Benchmarking:** Provides detailed metrics and resource analytics.
- **Automatic GPU Memory Cleanup:** Frees up GPU resources after model operations.
- **Session Management & Configurable Logging:** Enables tracking of model sessions and custom logging configurations.
- **Environment Variable Support:** Easily override settings through environment variables.

## Requirements

- Python 3.8 or higher
- [PyTorch](https://pytorch.org/)
- [PyYAML](https://pyyaml.org/)
- [psutil](https://pypi.org/project/psutil/)
- [jsonschema](https://pypi.org/project/jsonschema/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chafiq-dev/neurokit.git
   cd neurokit
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the package:**
   ```bash
   python setup.py install
   ```

## Usage

### Command Line Arguments

Run NeuroKit from the command line with the following options:
```bash
python -m neurokit --model-path PATH_TO_MODEL [options]
```

**Available options:**
- `--model-path PATH`: **(Required)** Path to your GGUF model file.
- `--config PATH`: Load settings from a JSON or YAML configuration file.
- `--benchmark`: Run performance benchmarking tools.
- `--quantize {4bit,8bit}`: Apply model quantization.
- `--cache-dir PATH`: Specify a directory for caching models.
- `--diagnostics`: Launch diagnostics mode for system monitoring.
- `--cleanup`: Trigger automatic GPU memory cleanup.

### Configuration File

NeuroKit supports both JSON and YAML configuration formats. Below is an example of a YAML configuration:

```yaml
model:
  path: "path/to/model.pth"
  quantization: "8bit"
  checksum: "your_model_checksum_here"

cache:
  directory: "./cache"

performance:
  benchmarking: true
  gradient_checkpointing: true

monitoring:
  diagnostics: true

logging:
  level: "INFO"
```

Or a JSON configuration:
```json
{
  "model": {
    "path": "path/to/model.pth",
    "quantization": "4bit",
    "checksum": ""
  },
  "cache": {
    "directory": "./cache"
  },
  "performance": {
    "benchmarking": true,
    "gradient_checkpointing": true
  },
  "monitoring": {
    "diagnostics": true
  },
  "logging": {
    "level": "INFO"
  }
}
```

Then run:
```bash
python -m neurokit --config config.yaml
```

## Model Optimization

NeuroKit optimizes model performance by:
- Automatically selecting the best device (GPU or CPU) based on hardware availability.
- Applying model quantization (4-bit or 8-bit) to balance performance and resource usage.
- Enabling gradient checkpointing for large models to save memory.
- Dynamically managing GPU memory and adjusting system resources based on real-time monitoring.

## Logging

All operations are logged with detailed information including:
- Model loading status and configuration details.
- Performance benchmarking and resource utilization.
- Error messages, warnings, and recovery steps.
- Diagnostic outputs for memory, GPU, and temperature metrics.

Logs can be viewed on the console or redirected to a file as needed.

## System Monitoring

NeuroKit provides real-time monitoring of:
- **Memory Usage:** Tracks total, used, and available system memory.
- **GPU Utilization:** Monitors GPU memory and device properties.
- **Temperature Metrics:** Reports system and GPU temperatures.
- **Performance Benchmarks:** Measures execution times and resource allocation.

## Contributing

Contributions are welcome! Please submit issues or pull requests for improvements, bug fixes, or new features. For detailed development guidelines, refer to the documentation provided in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
