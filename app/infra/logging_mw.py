import time, json, os
from starlette.middleware.base import BaseHTTPMiddleware
DEBUG_TRACE = os.getenv("DEBUG_TRACE","true").lower() == "true"

class JsonTraceMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if DEBUG_TRACE: print(json.dumps({"evt":"request","m":request.method,"p":request.url.path}))
        t=time.time(); resp=await call_next(request)
        if DEBUG_TRACE: print(json.dumps({"evt":"response","s":resp.status_code,"ms":round((time.time()-t)*1000,2)}))
        return resp
