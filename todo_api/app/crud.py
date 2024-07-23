from sqlalchemy.orm import Session
from . import schemas, models, database

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def getPage(id : int , db : Session):
    item_data=db.query(models.Items).filter(models.Items.id == id).first()
    return item_data

def postPage(item: schemas.ItemCreate , db : Session):
    db_item = models.Items(
        title=item.title, 
        description=item.description, 
        due_date=item.due_date, 
        status=item.status
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def putPage(id : int , item : schemas.ItemUpdate , db = Session):
    db_data=db.query(models.Items).filter(models.Items.id == id).first()
    if db_data is None :
        return None
    for key , value in item.dict().items():
        setattr(db_data,key,value)
    db.commit()
    db.refresh(db_data)
    return db_data

def deletePage(id : int , db : Session):
    db_item = db.query(models.Items).filter(models.Items.id == id).first()
    if db_item is None:
        return None
    db.delete(db_item)
    db.commit()
    return db_item