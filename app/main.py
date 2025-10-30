from fastapi import FastAPI
from .infra.logging_mw import JsonTraceMiddleware
from .controllers.notify_controller import router

app = FastAPI(title="Notifier Telegram")
app.add_middleware(JsonTraceMiddleware)
app.include_router(router)

@app.get("/health")
def health(): return {"ok": True}
