from fastapi import APIRouter, UploadFile, HTTPException
from models import Transcription
from utils import get_timestamp
import whisper
import os
import subprocess


router = APIRouter()


try:
    model = whisper.load_model("base")
    model_status = "loaded"
    print(f"STATUS: {model_status}")
except Exception as e:
    model = None
    model_status = "not loaded"
    print(f"Error: {e}")

try:
    result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, check=True)
    print("FFmpeg is working.")
except Exception as e:
    print("FFmpeg is not accessible:", e)


@router.post("/",
            response_model=Transcription,
            responses={
                400: {
                     "description": "Bad Request. Only '.wav' files are allowed.",
                     "content": {
                         "application/json": {
                             "example": {"detail": "The file must be '.wav'"}
                         }
                     }
                },
                422: {
                    "description": "Unprocessable Content.",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Error during transcription"}
                        }
                    }
                },
                500: {
                    "description": "Internal Server Error.",
                    "content": {
                        "application/json": {
                            "example": {"detail": "Whisper is not loaded"}
                        }
                    }
                },
            },
        )
async def transcription_to_text(file: UploadFile):
    if model_status != "loaded":
        raise HTTPException(status_code=500, detail="Whisper is not loaded")
    
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="The file must be '.wav'")


    try:
        temp_file = f"temp_{file.filename}"
        with open(temp_file, "wb") as f:
            f.write(file.file.read())    
        
        try:
            result = model.transcribe(temp_file)
            print("Transcription OK.")
        except RuntimeError as e:
            print("Transcription failed.")
            raise HTTPException(status_code=422, detail=f"Error during transcription: {e}")
        
        return Transcription(name=file.filename, text=result["text"], timestamp=get_timestamp())
    
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=f"File not found: {e}")
    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"Validation error: {e}")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)