from sqlalchemy import Column, SmallInteger, String, Date, Integer, Text
from sqlalchemy.orm import relationship
from config.model_global import Base


class User(Base):
    __tablename__ = "USER"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
