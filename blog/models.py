from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    published = Column(Boolean, default=False)
