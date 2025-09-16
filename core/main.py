from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

id = 0
db = {}

class ValueInput(BaseModel):
    description: str
    amount: float

class IdInput(BaseModel):
    id: int

class SingleResponse(BaseModel):
    return_value: dict

@app.post("/create/",response_model=ValueInput)
def create_value(data:ValueInput):
    global id
    id += 1
    db[id] = {"description": data.description, "amount": data.amount}
    return db[id]

@app.get("/values/")
def all_values():
    return db

@app.get("/values/{id: int}/")
def get_values(id):
    return_value = {"message": "not found"}
    if id in db.keys():
        return_value = {id : db[id]}
    return return_value

@app.put("/values/{id:int}/")
def get_values(id, description: str = Form(), amount : float = Form()):
    return_value = {"message": "not found"}
    if id in db.keys():
        db[id] = {"description": description, "amount": amount}
        return_value = {id : db[id]}
    return return_value

@app.delete("/values/{id:int}/")
def get_values(id):
    return_value = {"message": "not found"}
    if id in db.keys():
        db.pop(id)
        return_value = {"message": "success"}
    return return_value