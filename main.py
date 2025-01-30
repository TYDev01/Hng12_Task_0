import os
PORT = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.endpoint import router as info_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],

)

app.include_router(info_router, prefix="", tags=["Infos"])

