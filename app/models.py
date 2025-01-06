from pydantic import BaseModel
from datetime import datetime


class VersionResponse(BaseModel):
    api_version: str
    timestamp: str
    

class Transcription(BaseModel):
    name: str
    text: str
    timestamp: datetime
