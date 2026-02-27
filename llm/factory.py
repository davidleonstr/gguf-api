from llama_cpp import Llama
from llm.config import Config
from pathlib import Path

class Factory:
    def __init__(self, config: Config) -> None:
        self.path = Path(config.model_path)
        self.config = config

        # If model not found
        if not self.path.exists():
            raise FileNotFoundError(self.path)

        # If not gguf model
        if not self.path.suffix == '.gguf':
            raise Exception(f"'{self.path.resolve()}' is not a GGUF LLM model")   

    def get(self) -> Llama:
        # Create model
        model = Llama(**self.config.model_dump())

        # Return model
        return model