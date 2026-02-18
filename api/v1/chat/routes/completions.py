from flask import request
from api.v1.chat import chatbp
from api.v1.chat.controllers import ChatCompletionsController

@chatbp.route('/completions', methods=['POST'])
def completions():
    data = request.json
    return ChatCompletionsController(data=data).completions()
