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
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  "stream": false,
  "temperature": 0.7
}

```

**Response Example:**

```json
{
  "id": "chatcmpl-...",
  "object": "chat.completion",
  "created": 1715600000,
  "model": "./models/llama-3-8b.gguf",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 9,
    "total_tokens": 21
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