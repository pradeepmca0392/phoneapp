from twilio.rest import TwilioRestClient

TWILIO_PHONE_NUMBER = "+12183775799"

DIAL_NUMBERS = ["+918344135250"]

TWIML_INSTRUCTIONS_URL = \
  "https://demo.twilio.com/docs/classic.mp3"

client = TwilioRestClient("ACa0ed575f745862b4bbae11e2c40b5632", "f2a61f7adc140e4ac94195227821e949")

def dial_numbers(numbers_list):
    for number in numbers_list:
        print("Dialing " + number)
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER, url=TWIML_INSTRUCTIONS_URL, method="GET")

if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)