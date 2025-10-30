from abc import ABC, abstractmethod
from typing import Optional

class MessageSender(ABC):
    @abstractmethod
    async def send_message(self, chat_id: str, text: str, parse_mode: Optional[str]=None, silent: bool=False) -> dict: ...
