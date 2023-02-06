from fastapi import FastAPI
from pydantic import BaseModel
import datetime
import sqlalchemy
import databases


app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    # created_at: datetime.datetime
    # updated_at: datetime.datetime

class Poll(BaseModel):
    title: str
    type: str
    is_voting_active: bool
    is_add_choices_active: bool
    created_by: int
    # created_at: datetime.datetime
    # updated_at: datetime.datetime

@app.get("/")
async def root():
    return {"message": "hello world"}
    
@app.get("/polls")
async def root():
    return {"polls": "hello world"}

@app.get("/users")
async def root():
    return {"users": "hello world"}


@app.post("/users/")
async def create_user(user: User):
    return user


@app.post("/polls/")
async def create_poll(poll: Poll):
    return poll