from typing import Any

from fastapi import FastAPI
from numpy import random

from deta_fastapi.random import random_letter


app = FastAPI()


@app.get("/")
def read_root() -> dict[str, Any]:
    return {"Hello": "World"}


@app.get("/items/all")
def read_all_items() -> list[dict[str, Any]]:
    return [{"Hello": "World"}, {"Bye": "World"}]


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, Any]:
    return {"item_id": item_id}


@app.get("/random/int")
def read_random_int() -> dict[str, Any]:
    return {"int": random.randint(low=0, high=10)}


@app.get("/random/letter")
def read_random_letter() -> dict[str, Any]:
    return {"letter": random_letter()}
