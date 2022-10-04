local:
  uvicorn --host=localhost --port=8000 --reload --app-dir=src \
    deta_fastapi.main:app

deta-new:
  deta new --name=test2 --python src/deta_fastapi
