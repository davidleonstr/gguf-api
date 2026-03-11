<div align="center">
  <img src="resources/svg/app.svg" alt="Box Icon" width="180"/>
  <br/>
  
  <h3>Experimental Flask API to GGUF LLM models</h3>

  [![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

# GGUF-API

A high-performance, Flask-based API wrapper for serving GGUF (Llama.cpp) models with an OpenAI-compatible interface. This project allows you to transform local GGUF models into a scalable web service with support for streaming and complex model configurations.

## Features

* **OpenAI-Compatible Chat Completions:** Implements the `/v1/chat/completions` endpoint.
* **Streaming Support:** Real-time token streaming using Server-Sent Events (SSE).
* **Dynamic Model Loading:** Configure model parameters (n_ctx, n_gpu_layers, etc.) directly via CLI.
* **Pydantic Validation:** Strict request/response validation for data integrity.

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/davidleonstr/gguf-api.git
cd gguf-api

```

2. **Install Dependencies:**
Ensure you have the appropriate `llama-cpp-python` backend installed for your hardware (CPU, CUDA, or Metal).
```bash
pip install flask pydantic llama-cpp-python

```

---

## Usage

Start the server by pointing it to a valid `.gguf` model file. You can pass any `llama-cpp-python` parameter using the `--llm-params` flag.

### Basic Start

```bash
python main.py --host 0.0.0.0 --port 9000 --llm-params model_path=./models/llama-3-8b.gguf

```

### Advanced Hardware Acceleration

```bash
python main.py \
  --host 127.0.0.1 \
  --port 8080 \
  --logs \
  --llm-params \
  model_path=./models/mixtral.gguf \
  n_gpu_layers=33 \
  n_ctx=4096 \
  flash_attn=True

```

### Argument Reference

| Argument | Shortcut | Default | Description |
| --- | --- | --- | --- |
| `--host` | `-H` | `localhost` | The interface to bind to. |
| `--port` | `-p` | `9000` | The port to listen on. |
| `--logs` |  | `False` | Flag to enable file-based logging. |
| `--logs-file` | `-lf` | `log.log` | Path to the log file. |
| `--llm-params` | `-llp` | N/A | Key=Value pairs for model initialization. |

---

## API Endpoints

### Post Chat Completion

`POST /v1/chat/completions`

**Request Body Example:**

```json
{
    "model": "GPT-4.5",
    "messages": [
        {
            "role": "assistant",
            "content": "Hello"
        }
    ]
}
```

**Response Example:**

```json
{
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "How can I assist you today?",
                "name": null,
                "role": "assistant"
            }
        }
    ],
    "created": 1773249711,
    "id": "chatcmpl-c0a622c0-1f7d-4d85-8484-7ac4624893ac",
    "model": "GPT-4.5",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 7,
        "prompt_tokens": 36,
        "total_tokens": 43
    }
}
```

### Post Completion

`POST /v1/completion`

**Request Body Example:**

```json
{
    "model": "GPT-4.5",
    "prompt": "User: Hello\nAssitant:"
}
```

**Response Example:**

```json
{
    "choices": [
        {
            "finish_reason": "length",
            "index": 0,
            "logprobs": null,
            "text": " Hello! Welcome to our chat! How can I help you today? Do you"
        }
    ],
    "created": 1773249798,
    "id": "cmpl-e7dfdd94-1ab0-4a76-99bd-b36020a09fb9",
    "model": "GPT-4.5",
    "object": "text_completion",
    "usage": {
        "completion_tokens": 16,
        "prompt_tokens": 8,
        "total_tokens": 24
    }
}
```

---

## Logging System

When enabled via `--logs`, the system generates detailed logs with timestamps:

* `[INFO]`: Model loading stages and API status.
* `[ERROR]`: Inference failures or invalid request parameters.
* `[CRITICAL]`: Model file not found or initialization crashes.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.