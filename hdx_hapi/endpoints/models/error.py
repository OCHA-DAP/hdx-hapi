from typing import Any, Dict, List
from pydantic import BaseModel
from fastapi import status

class BadRequestResponse(BaseModel):
    detail: str

class ResponseValidationResponse(BaseModel):
    error_sample_list: List
    error: str


ERROR_RESPONSES: Dict[int, Dict[str, Any]] = {
    status.HTTP_400_BAD_REQUEST: {
        'model': BadRequestResponse,
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        'model': ResponseValidationResponse,
    },
}