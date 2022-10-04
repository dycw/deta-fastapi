import sys  # noqa: INP001


sys.path.append("src")


from deta_fastapi.app import get_app  # isort: skip  # noqa


app = get_app()
