from typing import List, Dict, Optional, Union, Any
from pydantic import BaseModel, ConfigDict
import llama_cpp

class Config(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra='allow'
    )

    model_path: str
    
    n_gpu_layers: int = -1
    split_mode: int = llama_cpp.LLAMA_SPLIT_MODE_LAYER
    main_gpu: int = 0
    tensor_split: Optional[List[float]] = None
    vocab_only: bool = False
    use_mmap: bool = True
    use_mlock: bool = False
    kv_overrides: Optional[Dict[str, Union[bool, int, float, str]]] = None
    seed: int = llama_cpp.LLAMA_DEFAULT_SEED
    n_ctx: int = 2048
    n_batch: int = 512
    n_ubatch: int = 512
    n_threads: Optional[int] = None
    n_threads_batch: Optional[int] = None
    rope_scaling_type: Optional[int] = llama_cpp.LLAMA_ROPE_SCALING_TYPE_UNSPECIFIED
    pooling_type: int = llama_cpp.LLAMA_POOLING_TYPE_UNSPECIFIED
    rope_freq_base: float = 0.0
    rope_freq_scale: float = 0.0
    yarn_ext_factor: float = -1.0
    yarn_attn_factor: float = 1.0
    yarn_beta_fast: float = 32.0
    yarn_beta_slow: float = 1.0
    yarn_orig_ctx: int = 0
    logits_all: bool = False
    embedding: bool = False
    offload_kqv: bool = True
    flash_attn: bool = False
    op_offload: Optional[bool] = None
    swa_full: Optional[bool] = None
    no_perf: bool = False
    last_n_tokens_size: int = 64
    lora_base: Optional[str] = None
    lora_scale: float = 1.0
    lora_path: Optional[str] = None
    numa: Union[bool, int] = False
    chat_format: Optional[str] = None

    chat_handler: Optional[Any] = None
    draft_model: Optional[Any] = None
    tokenizer: Optional[Any] = None

    type_k: Optional[int] = None
    type_v: Optional[int] = None
    spm_infill: bool = False
    verbose: bool = False