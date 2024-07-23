from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models, database, crud

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/",response_model=schemas.Item)
async def postPage(item:schemas.ItemCreate , db: Session = Depends(get_db)):
    return crud.postPage(db=db,item=item)

@app.get("/",response_model=schemas.Item)
async def getPage(id : int , db: Session = Depends(get_db)):
    item_data=crud.getPage(id=id,db=db)
    if item_data is None :
        raise HTTPException(status_code=404, detail="Page not found")
    return item_data

@app.put("/",response_model=schemas.Item)
async def putPage(id : int , item:schemas.ItemUpdate , db: Session = Depends(get_db)):
    item_data=crud.putPage(id=id,item=item,db=db)
    if item_data is None :
        raise HTTPException(status_code=404, detail="Item not found")
    return item_data

@app.delete("/",response_model=schemas.Item)
async def deletePage(id : int , db: Session = Depends(get_db)):
    item_data=crud.deletePage(id=id,db=db)
    if item_data is None :
        raise HTTPException(status_code=404, detail="Item not found")
    return item_data