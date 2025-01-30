from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.endpoint import router as info_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],

)

app.include_router(info_router, prefix="/home", tags=["Infos"])

