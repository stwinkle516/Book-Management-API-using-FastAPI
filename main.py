from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return{"Message":"Hello World"}

@app.get("/greet/{name}")
def greet(name:str, age:Optional[int] = None):
    return {"messeage":f"Hello {name} your age {age}"}

#
class Student(BaseModel):
    name:str
    age:int
    roll:int

@app.post("/create_student")
def create_student(student: Student):
    return {
        "name":student.name,
        "age":student.age,
        "roll":student.roll
    }
