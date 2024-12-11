from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_username = 'root'
database_password = ''
database_host = 'localhost'
database_port = '3307'
database_name = 'library'

engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.
    format(database_username, database_password, database_host, database_port, database_name))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
