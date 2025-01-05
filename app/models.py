from pydantic import BaseModel
from pydantic import field_validator
from datetime import datetime


class VersionResponse(BaseModel):
    api_version: str
    timestamp: datetime
    
    # @field_validator("timestamp")
    # def format_timestamp(cls, value):
    #     if isinstance(value, datetime):
    #         return value.strftime("%Y-%m-%d %H:%M:%S")
    #     return value
    

class Transcription(BaseModel):
    name: str
    text: str
    timestamp: datetime
