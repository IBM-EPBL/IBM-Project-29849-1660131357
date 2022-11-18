from datetime import datetime
from flask import request,after_this_request
from flask_restful import Resource
from utils.dbQuery import insertQuery
from utils.emailSender import newEmailSender
from utils.password import genHash

class Register(Resource):
    def post(self):
        req=request.json
        name=req['name']
        email=req['email']
        password=req['password']
        favourite=req['favourite']
        fav=','.join(favourite)
        if(name=='' or email=='' or password=='' or fav==''):
            return {"status":"Missing data"},404
        password=genHash(password)
        t=(name,email,password,fav,datetime.now())
        res=insertQuery('INSERT INTO user (name,email,password,favourites,resend_time) values (?,?,?,?,?)',t)
        if(not res):
            return {"status":"Error while registering"},400
        
        @after_this_request
        def emailer(response):
            newEmailSender(email)
            return response
        
        return {"status":"Successfully registered"},200