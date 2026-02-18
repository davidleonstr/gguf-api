from flask import Flask

from api.v1 import v1bp
from api.config import Config

# For typing
from llama_cpp import Llama

from utils import Log

def make(config: Config, llm: Llama, logs: Log) -> None:
    # Create app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(v1bp, url_prefix='/v1')

    # Informative logs
    if config.logs:
        logs.write(f'Setting Flask App globals.')

    # Set globals in app
    app.apiConfig = config
    app.llm = llm
    app.logsFile = logs

    # Informative logs
    if config.logs:
        logs.write(f'Running API.')

    # Set app basics
    app.run(host=config.host, port=config.port)

    # Informative logs
    if config.logs:
        logs.write(f'API closed.')