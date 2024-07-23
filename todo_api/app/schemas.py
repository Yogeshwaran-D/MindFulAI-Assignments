from pydantic import BaseModel
from datetime import datetime

# --------------Base class for Item--------------------#
class ItemBase(BaseModel):
    title: str
    description: str
    due_date: datetime
    status: bool
# --------------Create class for Item--------------------#
class ItemCreate(ItemBase):
    pass
# --------------Update class for Item--------------------#
class ItemUpdate(ItemBase):
    pass
# -----converts data from database into dictionaries-----#
class ItemInDataBase(ItemBase):
    id: int
    class Config:
        orm_mode = True
# -------------- Main class for Item----------------------#
class Item(ItemInDataBase):
    pass