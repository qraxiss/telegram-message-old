import api.controllers.message as controller
from flask import current_app as app
from flask_restful import Api

api = Api(app)

api.add_resource(controller.SendMessage, '/send-message')