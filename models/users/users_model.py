from sqlalchemy import Column, SmallInteger, String, Date, Integer, Text
from sqlalchemy.orm import relationship
from config.model_global import Base


class User(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
