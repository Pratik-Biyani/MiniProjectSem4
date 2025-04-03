import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
MY_WHATSAPP_NUMBER = os.getenv("MY_WHATSAPP_NUMBER")
RECEIVER_WHATSAPP_NUMBER = os.getenv("RECEIVER_WHATSAPP_NUMBER")
