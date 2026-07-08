from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_title = Column(String, unique=True)
    description = Column(String)
    assigned_to = Column(String)   # Changed from Integer
    priority = Column(String)
    status = Column(String)
    due_date = Column(String)
    created_by = Column(String)