from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models, schemas
from .db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    name: str
    price: int
    inventory: int

try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Vshnugraha21', cursor_factory= RealDictCursor)
    cursor = conn.cursor()
    print("Database Connection Was Succesfull")
except Exception as error:
    print("Connection To DB was Failed")
    print("Error", error)
    

@app.get("/")
async def root():
    return {"message": "Hello Brow"}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Products).all()
    return{"data": posts}

@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM products """)
    posts = cursor.fetchall()
    print(posts)
    return(posts)

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Response)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO products (name, price, inventory) VALUES  (%s, %s, %s) RETURNING * """,
    #                (post.name, post.price, post.inventory)
    #                )
    # new_post = cursor.fetchone()
    # conn.commit()
    new_post = models.Products(name=post.name, price=post.price, inventory=post.inventory)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return schemas.Response(name=new_post.name, price=new_post.price, id=new_post.id)

@app.post("/create")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"message" : "success..." f"title {payload['title']}"}