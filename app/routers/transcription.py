from fastapi import APIRouter, UploadFile, HTTPException
from models import Transcription
from utils import get_timestamp
import whisper
import os


router = APIRouter()


try:
    model = whisper.load_model("base")
    model_status = "loaded"
    print(f"STATUS: {model_status}")
except Exception as e:
    model = None
    model_status = "not loaded"
    print(f"Error: {e}")
    
# Absolutní cesta ke složce app/routers
current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = current_dir


@router.post("/", response_model=Transcription)
async def transcription_to_text(file: UploadFile):
    if model_status != "loaded":
        raise HTTPException(status_code=500, detail="Whisper is not loaded")
    
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="The file must be '.wav'")

    try:
        temp_file = os.path.join(target_dir, f"temp_{file.filename}")
        with open(temp_file, "wb") as f:
            f.write(file.file.read())

        print(f"TEMPORARY FILE PATH: {temp_file}")
        print(f"File exists: {os.path.exists(temp_file)}")
        print(f"Current working directory: {os.getcwd()}")
    
        
        result = model.transcribe(temp_file)
        print(result)
        
        os.remove(temp_file)
        
        return Transcription(name=file.filename, text="result[text]", timestamp=get_timestamp())
    except FileNotFoundError:
        # os.remove(temp_file)
        raise HTTPException(status_code=500, detail="Temporary file was not created.")
    except Exception as e:
        os.remove(temp_file)
        return HTTPException(status_code=500, detail=f"Error: {e}")
