from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def homepage():
  return {"message":"Hello World"}

