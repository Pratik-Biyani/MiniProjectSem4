from twilio.rest import Client
from TwilioDemo.config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

def send_whatsapp(recipient_number, voter_name):
    """
    Sends a WhatsApp message to a voter confirming their vote.

    :param recipient_number: The voter's WhatsApp number (e.g., "whatsapp:+919892765476")
    :param voter_name: The voter's name
    """
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message_body = f"Dear {voter_name}, ✅\n\nYou have successfully voted! 🗳️\n\nThank you for participating in the election."

    try:
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,  
            body=message_body,
            to=recipient_number  # Ensure it's already formatted as "whatsapp:+91XXXXXXXXXX"
        )
        print(f"✅ WhatsApp message sent to {recipient_number}")
    except Exception as e:
        print(f"❌ Error sending WhatsApp message: {e}")
