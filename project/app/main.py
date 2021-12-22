import uvicorn
from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI()


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
