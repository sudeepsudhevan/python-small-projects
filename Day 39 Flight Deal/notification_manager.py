from twilio.rest import Client

TWILIO_SID = "Your Token sid"
TWILIO_AUTH_TOKEN = "Your Auth token"
TWILIO_VIRTUAL_NUMBER = "your virtual number"
TWILIO_VERIFIED_NUMBER = "Your number"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
