from fastapi import APIRouter,HTTPException
from models import Status
from .transcription import model_status, error_message
from utils import get_timestamp


router = APIRouter()


@router.get(
    "/",
    response_model=Status,
    responses={
        200: {
            "description": "The model is loaded.",
            "content": {
                "application/json": {
                    "example": {
                        "status": "loaded",
                        "timestamp": "2025-01-02 10:00:00"
                    }
                }
            }
        },
        500: {
            "description": "Model not loaded.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": {
                            "status": "not loaded",
                            "error": "RuntimeError: Model basse not found.",
                            "timestamp": "2025-01-01 01:00:00"
                        }
                    }
                }
            }
        }
    }
)
def get_status():
    if model_status == "not loaded":
        raise HTTPException(
            status_code=500,
            detail={
                "status": model_status,
                "error": error_message,
                "timestamp": get_timestamp()
            }
        )
    return Status(
        status=model_status,
        timestamp=get_timestamp()
    )
