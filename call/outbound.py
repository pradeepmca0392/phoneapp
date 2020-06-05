# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = 'ACa0ed575f745862b4bbae11e2c40b5632'
auth_token = 'f2a61f7adc140e4ac94195227821e949'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='https://demo.twilio.com/docs/classic.mp3',
                        to='+918344135250',
                        from_='+12183775799',

                    )

print(call.sid)