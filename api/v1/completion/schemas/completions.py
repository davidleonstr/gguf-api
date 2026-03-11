from pydantic import BaseModel, Field
from typing import List, Optional, Union, Dict

from pydantic import BaseModel, Field
from typing import List, Optional, Union, Dict, Literal

class CompletionChoice(BaseModel):
    text: str
    index: int
    logprobs: Optional[Dict] = None
    finish_reason: Literal['stop', 'length', 'content_filter']

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class CompletionRequest(BaseModel):
    model: str = Field(...)
    prompt: Union[str, List[str], List[int], List[List[int]]] = "<|endoftext|>"
    
    suffix: Optional[str] = None
    max_tokens: Optional[int] = Field(default=16, gt=0)
    temperature: Optional[float] = Field(default=1.0, ge=0, le=2.0)
    top_p: Optional[float] = Field(default=1.0, ge=0, le=1.0)
    stream: Optional[bool] = Field(default=False)
    logprobs: Optional[int] = Field(default=None, ge=0, le=5)
    echo: Optional[bool] = Field(default=False)
    
    stop: Optional[Union[str, List[str]]] = None
    presence_penalty: Optional[float] = Field(default=0, ge=-2.0, le=2.0)
    frequency_penalty: Optional[float] = Field(default=0, ge=-2.0, le=2.0)
    logit_bias: Optional[Dict[str, float]] = None

class CompletionResponse(BaseModel):
    id: str
    object: Literal['text_completion']
    created: int
    model: str
    choices: List[CompletionChoice]
    usage: Usage