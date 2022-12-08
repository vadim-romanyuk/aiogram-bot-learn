from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class MediaIds(Base):
    __tablename__ = 'Products'
    item_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    likes = Column(String(255))
    dislike = Column(String(255))
