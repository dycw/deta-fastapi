from typing import Any

from fastapi import APIRouter

from deta_fastapi.functions import get_random_int
from deta_fastapi.functions import get_random_letter


router = APIRouter(prefix="/random", tags=["random"])


@router.get("/int")
def read_random_int() -> dict[str, Any]:
    return {"int": get_random_int()}


@router.get("/letter")
def read_random_letter() -> dict[str, Any]:
    return {"letter": get_random_letter()}
