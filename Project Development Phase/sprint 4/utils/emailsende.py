from __future__ import print_function
from utils.tokener import generate_confirmation_token
import sib_api_v3_sdk
import app
from sib_api_v3_sdk.rest import ApiException
from datetime import datetime


def emailSender(email, token):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = app.data['mail_api_key']
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    msg = {}
    msg['Subject'] = "Verfiy your NewsTracker Account"
    msg['From'] = {"name": "News Tracker Dev Team",
                   "email": "verify@newstracker.com"}
    msg['To'] = [{"email": email}]
    msg['Text']=f'Please click this <a href="http://127.0.0.1:5500/frontend/pages/verify.html?token={token}">link</a> to verify your account'
    html = f"""\
    <html>
        <head></head>
        <body>
        <p>?????, for joining NewsTracker ??</p>
        <br>
        <p>Hurray??, you just registerd at NewsTracker<br><br>
        Please click the following link to verify your account:<br>
        <a href="http://127.0.0.1:5500/frontend/pages/verify.html?token={token}">Click Here to Verify ??</a>
        </p>
        <br>
        <p>??Note: This link expires within one hour from the time sent</p>
        <br><br>
        <p>Regrads,<br></p>
        <p><a href="https://localhost:5000">NewsTracker Dev Team</a></p>
        <br><br>
        <p>Email sent at {dt_string}</p>
        </body>
    </html>
    """
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=msg['To'], html_content=html, sender=msg['From'], subject=msg['Subject'],text_content=msg['Text'])
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


def newEmailSender(email):
    token = generate_confirmation_token(email)
    emailSender(email, token)