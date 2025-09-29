import os

from dotenv import load_dotenv

load_dotenv()

RABBITMQ_DEFAULT_USER=os.getenv('RABBITMQ_DEFAULT_USER', 'admin')
RABBITMQ_DEFAULT_PASS=os.getenv('RABBITMQ_DEFAULT_PASS', 'admin')

TG_TOKEN = os.getenv('TG_TOKEN', '')
CHAT_ID = os.getenv('CHAT_ID', '')