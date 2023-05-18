from flask_restful import Resource, request
import logic.models.message as message

from errors.handler import handler
    
class SendMessage(Resource):
    @handler
    def post(self):
        return message.send_msg(request.json)