# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC22f8c00925d651044debd6bcdc35511c'
auth_token = '5532e110265d96902e43e307ee2c7c7c'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+19722993163',
         to='+16179522400'
     )

print(message.sid)
