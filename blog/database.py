import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()












# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from dotenv import load_dotenv
# load_dotenv()

# # SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
# SQLALCHAMY_DATABASE_URL = os.getenv('DATABASE_URL')


# engine = create_engine(
#     SQLALCHAMY_DATABASE_URL,
#     #   connect_args={'check_same_thread': False}
#       )


# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


# Base = declarative_base()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


