# GGUF Model Predictor

## Description
The GGUF Model Predictor is a command-line tool for loading and running predictions with GGUF and PyTorch models. It provides an easy way to work with machine learning models and make predictions based on input data.

## Features
- Load GGUF and PyTorch models.
- Run predictions with options for half precision and CPU optimization.
- Simple command-line interface for easy usage.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/chafiq-dev/GGUF-MP.git
   cd GGUF-MP
   ```
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install torch  # Ensure PyTorch is installed
   ```

## Usage
To run the predictor, use the following command:
```bash
python gguf-mp.py <model_path> [--half] [--cpu]
```
- `<model_path>`: Path to the model file (.gguf or .pt).
- `--half`: Use half precision for the model (optional).
- `--cpu`: Optimize for older CPU (optional).

### Example
```bash
python main.py model.gguf --half
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
