from fastapi import APIRouter, HTTPException
import os

router = APIRouter()



db_directory = 'database'

@router.get("/category")
async def get_namespaces():
    try: 
        namespaces = [name for name in os.listdir(db_directory) if os.path.isdir(os.path.join(db_directory, name))]
        return {"namespaces": namespaces}
       
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")