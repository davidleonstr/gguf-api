from dataclasses import dataclass

# Dataclass to initialize configuration
@dataclass
class Config:
    host: str = 'localhost'
    port: int = 9000
    logs: bool = False