# GGUF Model Predictor

## Description
The GGUF Model Predictor is a Python utility for loading and running GGUF language models with PyTorch integration. It provides flexible options for optimizing model performance based on your system capabilities and hardware specifications, with support for both CPU and GPU acceleration.

## Features

- PyTorch integration with CUDA support for GPU acceleration
- Automatic model optimization based on system capabilities
- Support for multiple hardware vendors (Intel, NVIDIA, AMD)
- FP16 precision support for improved performance on compatible GPUs
- Interactive configuration wizard
- Optional GTK-based GUI interface
- Configurable via command-line arguments or JSON configuration file
- System prompt loading capability
- Comprehensive logging system
- Dynamic performance scaling based on available GPU/CPU resources

## Requirements

- Python 3.x
- PyTorch
- ctransformers
- psutil
- GTK3 (optional, for GUI support)
- PyGObject (optional, for GUI support)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/chafiq-dev/gguf-mp.git
cd gguf-mp
```

2. Install required dependencies:
```bash
pip install torch ctransformers psutil
```

3. For GUI support (optional):
```bash
# Ubuntu/Debian
sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0

# Fedora
sudo dnf install python3-gobject gtk3

# macOS
brew install gtk+3 pygobject3
```

## Usage

### Command Line Arguments

```bash
python gguf-mp.py --model-path PATH_TO_MODEL [options]
```

Available options:
- `--model-path PATH`: Path to your GGUF model file (required)
- `--gpu-performance {high,medium,low}`: Set GPU performance level (default: high)
- `--cpu-performance {high,medium,low}`: Set CPU performance level (default: high)
- `--hardware-vendor {intel,nvidia,amd,unspecified}`: Specify hardware vendor (default: unspecified)
- `--wizard`: Run interactive configuration wizard
- `--sys-prmpt PATH`: Load system prompt from file
- `--gui`: Launch GTK GUI interface
- `--config PATH`: Load settings from JSON configuration file

### Configuration File

Create a JSON file with your preferred settings:

```json
{
    "model-path": "/path/to/model.gguf",
    "gpu-performance": "high",
    "cpu-performance": "medium",
    "hardware-vendor": "nvidia"
}
```

Then run:
```bash
python gguf-mp.py --config config.json
```

### Interactive Wizard

Run the interactive configuration wizard:
```bash
python gguf-mp.py --wizard
```

## Model Optimization

The utility automatically optimizes model loading and inference based on:
- Available GPU memory (if CUDA is available)
- CPU resources
- System memory
- Selected performance profile

Optimization features include:
- Automatic FP16 conversion for high-performance GPU mode
- Dynamic CUDA memory management
- Adaptive performance settings based on available resources

## Logging

The utility logs all operations to `gguf_mp.log`. The log includes:
- Model loading status and configurations
- Performance detection results
- Configuration loading status
- System prompt loading status
- Error messages and warnings
- GPU/CPU optimization settings

## System Requirements

Minimum requirements:
- 4GB RAM for CPU mode
- 4GB VRAM for GPU mode (recommended: 8GB+ for larger models)
- Python 3.7 or higher
- CUDA-compatible GPU for GPU acceleration (optional)

The utility automatically detects system capabilities and adjusts settings based on:
- GPU memory and capabilities (if available)
- CPU usage and specifications
- Available system memory
- Hardware vendor specifications

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
