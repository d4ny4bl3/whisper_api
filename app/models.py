from pydantic import BaseModel


class VersionResponse(BaseModel):
    api_version: str
    timestamp: str
    

class Transcription(BaseModel):
    name: str
    text: str
    timestamp: str
    
    
class Status(BaseModel):
    status: str
    timestamp: str
