from fastapi import FastAPI
from routers import version, transcription
from fastapi import UploadFile

from utils import api_version


app = FastAPI(
    title="Whisper API",
    description="API for speech-to-text conversion using the Whisper",
    version=api_version
    )


app.include_router(version.router, prefix="/version", tags=["Version"])
app.include_router(transcription.router, prefix="/transcription", tags=["Transcription"])
