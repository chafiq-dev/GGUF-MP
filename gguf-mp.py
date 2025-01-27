#!/usr/bin/python3
import argparse
import os
import psutil
import logging
import json

# Attempt to import the gi library (GTK) if available
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
    GTK_AVAILABLE = True
except (ImportError, ValueError):
    GTK_AVAILABLE = False

# Configure logging
logging.basicConfig(
    filename='gguf_mp.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('gguf_mp.log'),
        logging.StreamHandler()
    ]
)

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Run the GGUF-MP model with specified performance settings and hardware configurations.")
    parser.add_argument('--gpu-performance', choices=['high', 'medium', 'low'], default='high',
                        help="Set GPU performance level. Choices are 'high', 'medium', or 'low'. Default is 'high'.")
    parser.add_argument('--cpu-performance', choices=['high', 'medium', 'low'], default='high',
                        help="Set CPU performance level. Choices are 'high', 'medium', or 'low'. Default is 'high'.")
    parser.add_argument('--hardware-vendor', choices=['intel', 'nvidia', 'amd', 'unspecified'], default='unspecified',
                        help="Specify hardware vendor. Choices are 'intel', 'nvidia', 'amd', or 'unspecified'. Default is 'unspecified'.")
    parser.add_argument('--wizard', action='store_true', help="Run the configuration wizard to set up the model interactively.")
    parser.add_argument('--sys-prmpt', type=str, help="Path to a file containing the system prompt to load.")
    parser.add_argument('--gui', action='store_true', help="Launch a simple GTK GUI for configuration.")
    parser.add_argument('--config', type=str, help="Path to a JSON configuration file.")
    return parser.parse_args()

def load_config(config_path: str) -> dict:
    """Load configuration from a JSON file."""
    if config_path and os.path.exists(config_path):
        with open(config_path, 'r') as file:
            config = json.load(file)
            logging.info(f"Configuration loaded from {config_path}")
            return config
    else:
        logging.error(f"Configuration file '{config_path}' not found.")
        return {}

def detect_system_capabilities() -> str:
    """Detect system capabilities based on CPU usage and memory."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024 ** 3)  # Convert to GB

    if cpu_usage > 80 or total_memory < 2:
        return 'low'
    elif cpu_usage > 50 or total_memory < 4:
        return 'medium'
    else:
        return 'high'

def load_system_prompt(file_path: str) -> str:
    """Load the system prompt from a file."""
    if file_path and os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        logging.error(f"System prompt file '{file_path}' not found.")
        return None

def wizard_mode() -> tuple:
    """Run the configuration wizard for user input."""
    print("Welcome to the configuration wizard.")
    gpu_perf = input("Select GPU performance (high/medium/low): ")
    cpu_perf = input("Select CPU performance (high/medium/low): ")
    vendor = input("Specify hardware vendor (intel/nvidia/amd/unspecified): ")
    return gpu_perf, cpu_perf, vendor

def main():
    args = parse_args()

    if not GTK_AVAILABLE:
        proceed = input("GTK is not supported or the gi library is not installed on your system. Use wizard mode instead? (Y/N): ").strip().lower()
        if proceed != 'y':
            logging.info("User chose not to proceed with wizard mode. Exiting.")
            print("Exiting the program.")
            return

    if args.wizard:
        gpu_perf, cpu_perf, vendor = wizard_mode()
    else:
        if args.config:
            config = load_config(args.config)
            if config:
                gpu_perf = config.get('gpu-performance', 'high')
                cpu_perf = config.get('cpu-performance', 'high')
                vendor = config.get('hardware-vendor', 'unspecified')
            else:
                logging.error("Invalid configuration. Exiting.")
                print("Invalid configuration. Exiting.")
                return
        else:
            gpu_perf = args.gpu_performance
            cpu_perf = args.cpu_performance
            vendor = args.hardware_vendor

    system_prompt = load_system_prompt(args.sys_prmpt)
    if system_prompt:
        logging.info(f"System prompt loaded from {args.sys_prmpt}")
    else:
        logging.warning("No system prompt loaded.")

    performance_mode = detect_system_capabilities()
    logging.info(f"Detected system performance mode: {performance_mode}")

    if performance_mode == 'low':
        logging.info("Applying low performance settings.")
        # Apply low performance settings
    elif performance_mode == 'medium':
        logging.info("Applying medium performance settings.")
        # Apply medium performance settings
    else:
        logging.info("Applying high performance settings.")
        # Apply high performance settings

if __name__ == "__main__":
    main()
