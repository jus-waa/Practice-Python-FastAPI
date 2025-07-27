#"blueprints" for what the db looks like (table design)
from sqlalchemy import Column, Integer, String, Text, Time, DateTime, 
from db_config import Base

class Intern(Base):
    __tablename__ = "intern"

    intern_id=Column(Integer, autoincrement=True, primary_key=True)
    intern_name=Column(String(255), nullable=False)
    