from flask import request
from flask_restful import Resource
from utils.dbQuery import selectQuery

class CheckEmail(Resource):
    def post(self):
        data=request.json
        email=str(data["email"])
        res=selectQuery("SELECT email FROM USER WHERE EMAIL=?",(email,))
        print(res)
        if(not res):
            return {"status":True},200
        return {"status":False},400