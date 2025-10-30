from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..domain.ports import MessageSender
from ..di import get_sender

router = APIRouter(prefix="/api/notify/telegram", tags=["telegram"])

class NotifyIn(BaseModel):
    chat_id: str
    text: str
    parse_mode: str | None = None
    silent: bool = False

@router.post("/send")
async def send(body: NotifyIn, sender: MessageSender = Depends(get_sender)):
    return await sender.send_message(body.chat_id, body.text, body.parse_mode, body.silent)
