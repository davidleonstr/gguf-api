from utils import Log

# Import api utilies
from api.config import Config as APIConfig
from api import make

# Import llm utilies
from llm.config import Config as LLMConfig
from llm.factory import Factory

import argparse

parser = argparse.ArgumentParser(description='gguf-api parser.')

# Read this help
parser.add_argument(
    '--host',
    '-H',
    default=APIConfig.host,
    type=str,
    help=f'API Host. Default (`{APIConfig.host}`).'
)

# Read this help
parser.add_argument(
    '--port', 
    '-p',
    default=APIConfig.port,
    type=int, 
    help=f'API Port. Default ({APIConfig.port}).'
)

# Read this help
parser.add_argument(
    '--logs',
    default=APIConfig.logs,
    action=argparse.BooleanOptionalAction,
    help=f'Flag to enable/disable logs in file. Actual ({APIConfig.logs}).'
)

# Read this help
parser.add_argument(
    '--logs-file', 
    '-lf',
    default='log.log',
    type=str, 
    help=f'Logs file path. Default (`log.log`).'
)

# Read this help
parser.add_argument(
    '--llm-params', 
    '-llp',
    nargs='*', 
    help='LLM model parameters using key=value. `llm_cpp.Llama` as reference.'
)

args = parser.parse_args()

def main(args):
    # Default file
    logs = Log(args.logs_file)

    # Make API Config
    APICONFIG = APIConfig(
        host=args.host,
        port=args.port,
        logs=args.logs
    )

    # Informative log
    if APICONFIG.logs:
        logs.write(f'Parsing LLM model parameters.')

    # Parse key=value as dict
    kwargs = {}
    if args.llm_params:
        for item in args.llm_params:
            # Item typing
            item: str
            key, value = item.split('=', 1)
            kwargs[key] = value

    # Make LLM Config from kwargs
    LLMCONFIG = LLMConfig(**kwargs)

    # Informative log
    if APICONFIG.logs:
        logs.write(f'LLM model configuration created successfully.')

    # Try make the model
    try:
        # Informative log
        if APICONFIG.logs:
            logs.write(f'Loading LLM model.')

        # Create LLM model
        LLM = Factory(LLMCONFIG)

        # Model path
        path = LLM.path

        # Llama bbject
        LLM = LLM.get()

        # Informative log
        if APICONFIG.logs:
            logs.write(f"LLM model loaded successfully. Model path: '{path.resolve()}'.")
    except Exception as e:
        if APICONFIG.logs:
            logs.write(f'Error initializing LLM model: {str(e)}.')
        
        # Raise after log
        raise e

    # Informative log
    if APICONFIG.logs:
        logs.write(f'Making API.')

    # Make API Service
    make(
        config=APICONFIG, 
        llm=LLM, 
        logs=logs
    )

if __name__ == '__main__':
    # Entry point
    main(args)