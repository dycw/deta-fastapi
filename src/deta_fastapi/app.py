from typing import Any

from fastapi import FastAPI

from deta_fastapi.routers import items
from deta_fastapi.routers import random


def get_app() -> FastAPI:
    app = FastAPI()
    register_routes(app)
    app.include_router(items.router)
    app.include_router(random.router)
    return app


def read_root() -> dict[str, Any]:
    return {"Hello": "World"}


def register_routes(app: FastAPI, /) -> None:
    _ = app.get("/")(read_root)
