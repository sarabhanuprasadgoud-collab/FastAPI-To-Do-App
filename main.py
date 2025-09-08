from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/")
asyc def get_all_todos():
  data = collection.find()
@app.include_router(router)
