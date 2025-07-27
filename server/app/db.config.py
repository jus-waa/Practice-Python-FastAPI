from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from settings import settings

#sets up the connection to the db
engine = create_engine(settings.DB_URL, echo=settings.DEBUG) 
#interface to talk to db, lets add, query, update, bind=engine connects session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
#base class for ORM models (Object Relational Mapping lets you work with db using python classes and obj)
Base = declarative_base 