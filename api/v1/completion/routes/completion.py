from flask import request
from api.v1.completion import completionbp
from api.v1.completion.controllers import ChatCompletionController

@completionbp.route('/completion', methods=['POST'])
def completions():
    data = request.json
    return ChatCompletionController(data=data).completions()
