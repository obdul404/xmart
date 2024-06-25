from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Server is up and running"}



@app.get("/new")
async def root():
    return {"message": "New page is up and running."}



@app.post("/add")
async def root2(data: str, data2: str):
    return {"message": 'Data received: ' + data + ' and ' + data2}