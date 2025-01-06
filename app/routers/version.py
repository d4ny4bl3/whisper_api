from fastapi import APIRouter, HTTPException
from models import VersionResponse

from utils import api_version, get_timestamp


router = APIRouter()


@router.get("/", response_model=VersionResponse)
def get_version():
    try:
        return VersionResponse(api_version=api_version, timestamp=get_timestamp())
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "error": str(e),
                "timestamp": get_timestamp()
            }
        )
