from app.config.database import Base, engine
from sqlalchemy import Column, String, Boolean
from datetime import datetime

class Book(Base):
    __tablename__ = 'book'

    isbn = Column(String(50), primary_key=True, index=True)
    title = Column(String(255), index=True)
    author = Column(String(255), index=True)
    year = Column(String(5), index=True)
    published = Column(Boolean, default=True)
    created = Column(String(50), default=datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

Base.metadata.create_all(bind=engine)
