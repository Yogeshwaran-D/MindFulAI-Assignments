from sqlalchemy import Column, String, Integer, DateTime , Boolean
from . database import Base

class Items(Base):
    __tablename__ = "todo_items"
    id = Column(Integer, primary_key=True)
    title = Column(String, default="This is Todo Item title")
    description = Column(String, default="This is Todo Item Description")
    due_date =  Column(DateTime)
    status = Column(Boolean,default=False)