from datetime import datetime
from flask_restful import Resource
from flask import request,after_this_request
from utils.password import checkPassword
from utils.dbQuery import *
from dateparser import parse
from utils.tokener import generate_confirmation_token
from utils.emailSender import emailSender
import app
import jwt

class Login(Resource):
    def post(self):
        data=request.json
        ip=request.headers.get("ip")
        email=data["email"]
        password=data["password"]
        queryRes=selectQuery("SELECT * from user where email=?",(email,))
        res=checkPassword(password,queryRes["PASSWORD"])
        if(not res):
            return {"status":"Wrong credentials"},400
        if(not queryRes["VERIFIED"]):
            lastTime=parse(queryRes["RESEND_TIME"])
            currTime=datetime.now()
            diff=currTime-lastTime
            diff=diff.total_seconds()
            if(diff>3600):
                token=generate_confirmation_token(email)
                emailSender(email,token)
                insertQuery("UPDATE user set RESEND_TIME=? where email=?",(datetime.now(),email))
            return {"status":"Not verified"},400

        @after_this_request
        def cookieSender(response):
            access_token=jwt.encode(
                {"email":email,"ip":ip},app.app.config['SECRET_KEY']
            )
            # response.set_cookie("access_token",str(access_token),httponly=True,samesite=None,path="/")
            # response.set_cookie("email",str(email),httponly=True,samesite=None,path="/")
            response.headers.add('Set-Cookie',f'access_token={str(access_token)}; SameSite=None; Secure; HttpOnly; Path=/')
            response.headers.add('Set-Cookie',f'email={str(email)}; SameSite=None; Secure; HttpOnly; Path=/')
            return response
        
        return{"status":"Successfully Logged in"},200        