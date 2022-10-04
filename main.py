from typing import Any  # noqa: INP001

from fastapi import FastAPI
from numpy import random


app = FastAPI()


@app.get("/")
def read_root() -> dict[str, Any]:
    return {"Hello": "World"}


@app.get("/items/all")
def read_all_items() -> list[dict[str, Any]]:
    return [{"Hello": "World"}, {"Bye": "World"}]


@app.get("/items/random")
def read_random_item() -> dict[str, Any]:
    id = random.randint(low=0, high=10)
    return {"item_id": id}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}
