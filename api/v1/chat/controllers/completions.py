from flask import Response as FlaskStreamResponse, stream_with_context, current_app
import json
from api.v1.chat.schemas import (
    ChatCompletionResponse, ChatCompletionErrorResponse,
    ChatCompletionError, ChatCompletionRequest
)
from api.tools import Response

class ChatCompletionsController:
    def __init__(self, data: dict) -> None:
        self.data = data

    def _error_response(self, message, error_type, status_code, param=None):
        error = ChatCompletionError(message=message, type=error_type, param=param)

        return Response(
            data=ChatCompletionErrorResponse(error=error).model_dump()
        ).send(status_code)

    def completions(self):
        try:
            request = ChatCompletionRequest(**self.data)
        except Exception as e:
            return self._error_response('Invalid request fields', 'invalid_request_error', 400, str(e))

        llm = getattr(current_app, 'llm', None)
        if not llm:
            return self._error_response('LLM Model not initialized', 'server_error', 500)

        try:
            # llm: Llama
            completion = llm.create_chat_completion(**request.model_dump())

            if request.stream:
                return self._handle_stream(completion)

            return Response(data=ChatCompletionResponse(**completion)).send(200)

        except Exception as e:
            if hasattr(current_app, 'logsFile') and current_app.apiConfig.logs:
                current_app.logsFile.write(str(e), type='error')

            return self._error_response('Internal Server Error', 'server_error', 500)

    def _handle_stream(self, completion):
        def generate():
            try:
                for chunk in completion:
                    yield f'data: {json.dumps(chunk)}\n\n'
                yield 'data: [DONE]\n\n'
            except Exception:
                error = ChatCompletionError(message='Stream Error', type='server_error')
                yield f'data: {json.dumps(error.model_dump())}\n\n'

        return FlaskStreamResponse(stream_with_context(generate()), mimetype='text/event-stream')