import os
from .infra.telegram_sender import TelegramSender
from .domain.ports import MessageSender

def get_sender() -> MessageSender:
    return TelegramSender(os.getenv("TELEGRAM_BOT_TOKEN",""))
