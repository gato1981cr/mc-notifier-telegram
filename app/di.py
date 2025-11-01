import os
from dotenv import load_dotenv
from .infra.telegram_sender import TelegramSender
from .domain.ports import MessageSender

load_dotenv()  # <-- agrega esta línea para cargar las variables del .env

def get_sender() -> MessageSender:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    return TelegramSender(token)
