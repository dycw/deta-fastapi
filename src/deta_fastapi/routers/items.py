from typing import Any

from fastapi import APIRouter


router = APIRouter(prefix="/items", tags=["items"])


@router.get("/all")
def read_all_items() -> list[dict[str, Any]]:
    return [{"Hello": "World"}, {"Bye": "World"}]


@router.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}
