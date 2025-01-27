# GGUF Model Predictor

## Description
The GGUF Model Predictor is a Python utility for running GGUF models with configurable performance settings and hardware configurations. It provides flexible options for optimizing model performance based on your system capabilities and hardware specifications.

## Features

- Dynamic performance optimization based on system capabilities
- Support for multiple hardware vendors (Intel, NVIDIA, AMD)
- Interactive configuration wizard
- Optional GTK-based GUI interface
- Configurable via command-line arguments or JSON configuration file
- System prompt loading capability
- Comprehensive logging system

## Requirements

- Python 3.x
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
pip install psutil
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
python gguf-mp.py [options]
```

Available options:
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

## Logging

The utility logs all operations to `gguf_mp.log`. The log includes:
- Performance detection results
- Configuration loading status
- System prompt loading status
- Error messages and warnings

## System Requirements

The utility automatically detects system capabilities and adjusts settings based on:
- CPU usage
- Available memory
- Hardware vendor specifications

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
