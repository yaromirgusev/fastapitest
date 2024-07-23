from typing import Optional
from pydantic import BaseModel, conint
from fastapi import FastAPI, Depends
import uvicorn
from database import SessionLocal, engine, Base
from routers import user as UserRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(UserRouter.router, prefix='/user')


if __name__ == '__main__':
    uvicorn.run('fastapitest:app', host='0.0.0.0', port=1488, reload=True, workers=6)
