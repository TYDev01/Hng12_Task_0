from fastapi import APIRouter, status
from datetime import datetime, timezone


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def home():
    email = "tonieschi@gmail.com"
    current_datetime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    github_url = "https://github.com/TYDev01/Hng12_Task_0"

    return {
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    }