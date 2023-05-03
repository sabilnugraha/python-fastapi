from .. import models, schemas
from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..db import engine, SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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