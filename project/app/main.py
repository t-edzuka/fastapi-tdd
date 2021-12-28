import os

import uvicorn
from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.config import get_settings, Settings

app = FastAPI()

register_tortoise(app,
                  db_url=os.environ.get('DATABASE_URL'),
                  modules={'models': ['app.models.tortoise']},
                  generate_schemas=False,
                  add_exception_handlers=True,
                  )


@app.get('/')
def root():
    return {'root': 'Hello'}


@app.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return {"ping": "pong!",
            'environment': settings.environment,
            'testing': settings.testing,
            }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
