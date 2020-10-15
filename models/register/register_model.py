from sqlalchemy import Column, SmallInteger, String, Date, Integer, Text
from sqlalchemy.orm import relationship
from config.model_global import Base


class Register(Base):
    __tablename__ = "register"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    email = Column(String)
    sex = Column(String)
    country = Column(String)