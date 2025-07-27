from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from settings import settings

engine = create_engine(settings.DB_URL, echo=settings.DEBUG) #sets up the connection to the db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #interface tot alk to db, lets add, query, update, delete
Base = declarative_base #base class for ORM models (Object Relational Mapping lets you work with db using python classes and obj)