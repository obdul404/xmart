from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
import os

DATABASE_URL = os.getenv("DATABASE_URL")

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
@app.get("/")
async def root():
    return {"App is Running with db connected."}
    
@app.get("/getUser", response_model=list[User])
async def root():
    with Session(engine) as session:
        heroes = session.exec(select(User)).all()
        return heroes

@app.post("/creUser")
def create_hero(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"This User Added to db."}
    
@app.put("/updUser")
def update_hero(user: User, id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == id)
        results = session.exec(statement)
        user_1 = results.one()
        user_1.age = user.age
        user_1.name = user.name
        user_1.secret_name = user.secret_name
        session.commit()
        session.refresh(user)
        return {"This User has been updated in db."}

@app.delete("/delUser")
def delete_hero(id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == id)
        results = session.exec(statement)
        user_1 = results.one()
        session.delete(user_1)
        session.commit()
        return {"This User has been delete from db."}