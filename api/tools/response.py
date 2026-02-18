from pydantic import BaseModel
from flask import jsonify
from flask import Response as FlaskResponse

class Response:
    def __init__(self, data: BaseModel) -> None:
        self.data = data
    
    def send(self, code: int = 200) -> FlaskResponse:
        # Model dump as dict
        response = self.data.model_dump()
        
        # Return response
        return jsonify(response), code