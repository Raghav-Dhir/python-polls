from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import datetime
from sqlalchemy.orm import Session
from db.models import models
from db.db import engine, SessionLocal
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(BaseModel):
    username: str
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserCreate(BaseModel):
    username: str
    email: str

class Poll(BaseModel):
    title: str
    type: str
    is_voting_active: bool
    is_add_choices_active: bool
    created_by: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/")
async def root():
    return {"message": "hello world"}
    
@app.get("/polls")
async def root():
    return {"polls": "hello world"}

@app.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@app.post("/polls/")
async def create_poll(poll: Poll):
    return poll