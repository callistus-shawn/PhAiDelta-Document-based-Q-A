from fastapi import HTTPException
db=None

def get_db():
    if(db==None):
        raise HTTPException(status_code=404,detail="file not found,upload file properly ")
    else:
        return db

