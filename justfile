local:
  uvicorn --host=localhost --port=8000 --reload main:app

deta-new:
  deta new --python

deploy:
  deta deploy
