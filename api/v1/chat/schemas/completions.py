from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Union, Dict

class ResponseFormat(BaseModel):
    type: str = Field(pattern='^(text|json_object)$')

class Message(BaseModel):
    role: Literal['system', 'user', 'assistant']
    content: Optional[str] = Field(None)
    name: Optional[str] = Field(None)

class Choice(BaseModel):
    index: int
    message: Message
    finish_reason: Literal['stop', 'length']

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class ChatCompletionError(BaseModel):
    message: str
    type: str
    param: str | None
    code: str | int | None = None

class ChatCompletionRequest(BaseModel):
    model: Optional[str] = None 
    messages: List[Message] = Field(..., min_length=1)
    
    temperature: Optional[float] = Field(default=1.0, ge=0, le=2.0)
    top_p: Optional[float] = Field(default=1.0, ge=0, le=1.0)
    stream: Optional[bool] = Field(default=False)
    
    stop: Optional[Union[str, List[str]]] = None
    max_tokens: Optional[int] = Field(default=None, gt=0)
    
    presence_penalty: Optional[float] = Field(default=0, ge=-2.0, le=2.0)
    frequency_penalty: Optional[float] = Field(default=0, ge=-2.0, le=2.0)
    
    response_format: Optional[ResponseFormat] = None
    seed: Optional[int] = None
    
    logprobs: Optional[bool] = False
    top_logprobs: Optional[int] = Field(default=None, ge=0, le=20)
    logit_bias: Optional[Dict[str, float]] = None

class ChatCompletionResponse(BaseModel):
    id: str
    object: Literal['chat.completion']
    created: int
    model: str
    choices: List[Choice]
    usage: Usage

class ChatCompletionErrorResponse(BaseModel):
    error: ChatCompletionError