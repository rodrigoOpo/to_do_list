from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

SQL_ALCHEMY_DATABASE_CONNECTION = os.getenv("POSTGRESQL_URL_CONNECTION")
engine = create_engine(SQL_ALCHEMY_DATABASE_CONNECTION)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


 