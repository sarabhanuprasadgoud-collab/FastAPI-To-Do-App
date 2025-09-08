from fastapi import FastAPI, APIRouter
from configrations import collection
from database.schemas import all_tasks
from database.models import Todo

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_todos():
  data = collection.find()
  return all_tasks(data)

@router.post("/")
async def create_task(new_task: Todo):
  
@app.include_router(router)
