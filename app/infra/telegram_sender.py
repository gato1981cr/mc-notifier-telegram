import os, httpx
from typing import Optional
from ..domain.ports import MessageSender

class TelegramSender(MessageSender):
    def __init__(self, token: str):
        self.base = f"https://api.telegram.org/bot{token}"

    async def send_message(self, chat_id: str, text: str, parse_mode: Optional[str]=None, silent: bool=False) -> dict:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(f"{self.base}/sendMessage", json={
                "chat_id": chat_id, "text": text, "parse_mode": parse_mode, "disable_notification": silent
            })
            r.raise_for_status()
            return r.json()
