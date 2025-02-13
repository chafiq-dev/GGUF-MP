# neurokit/__main__.py
import argparse
from neurokit.core.model_manager import ModelManager
from neurokit.config.config_manager import ConfigManager
from neurokit.monitoring.benchmark import run_benchmark
from neurokit.utils.logger import setup_logging

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="NeuroKit Neural Model Management Tool")
    parser.add_argument('--model-path', type=str, help="Path to the GGUF model")
    parser.add_argument('--config', type=str, help="Path to configuration file (JSON/YAML)")
    parser.add_argument('--benchmark', action='store_true', help="Run performance benchmark")
    parser.add_argument('--quantize', choices=['4bit', '8bit'], help="Apply quantization")
    parser.add_argument('--cache-dir', type=str, help="Directory for caching models")
    parser.add_argument('--diagnostics', action='store_true', help="Run diagnostics mode")
    parser.add_argument('--cleanup', action='store_true', help="Run GPU memory cleanup")
    args = parser.parse_args()

    if args.config:
        config_manager = ConfigManager(args.config)
        config = config_manager.load_config()
    else:
        config = {}

    if args.model_path:
        mm = ModelManager(model_path=args.model_path, config=config, cache_dir=args.cache_dir)
        mm.load_model()
        if args.quantize:
            mm.quantize_model(args.quantize)
    
    if args.benchmark:
        run_benchmark()

    if args.cleanup:
        from neurokit.utils.env import cleanup_gpu_memory
        cleanup_gpu_memory()

    if args.diagnostics:
        from neurokit.monitoring.system_monitor import run_diagnostics
        run_diagnostics()

if __name__ == "__main__":
    main()
