FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install flask
RUN pip3 install ibm_db
RUN pip3 install flask_sqlalchemy
RUN pip3 install flask_bcrypt
RUN pip3 install flask_login
RUN pip3 install flask_wtf
RUN pip3 install wtforms

WORKDIR /main

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]


