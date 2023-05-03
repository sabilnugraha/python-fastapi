from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .db import Base

class Products(Base):
    __tablename__ = "products"

    name = Column(String, nullable=False)
    price = Column(String, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    inventory = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('nom()'))
