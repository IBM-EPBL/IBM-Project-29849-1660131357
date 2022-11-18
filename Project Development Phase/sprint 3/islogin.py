from flask import request, after_this_request
from utils.password import checkPassword
from flask_restful import Resource
from utils.cookieChecker import token_required


class IsLogin(Resource):
    @token_required
    def get(email, self):
        return {"status": "Logged in"}, 200