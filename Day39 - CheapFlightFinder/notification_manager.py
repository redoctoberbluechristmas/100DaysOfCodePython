from twilio.rest import Client


class NotificationManager:
    def __init__(self, sms_sid, sms_token, source_phone_number, dest_phone_number):
        self.sms_sid = sms_sid
        self.sms_token = sms_token
        self.source_phone_number = source_phone_number
        self.dest_phone_number = dest_phone_number
        self.twilio_client = Client(self.sms_sid, self.sms_token)


    def send_notification(self, destination, price):

        message = f"New cheap flight to {destination}. Price is {price}"
        print(message)
        self.twilio_client.messages.create(
            body=message,
            from_=self.source_phone_number,
            to=self.dest_phone_number
        )