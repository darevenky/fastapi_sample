from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {
    1: {
        'name' : 'venky',
        'age' : 25
    },

    2: {
        'name' : 'dare',
        'age' : 26
    }
}

class Student(BaseModel):
    name : str
    age : int

class Update_student(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None

#get the all the students data
@app.get("/")
def venky():
    return students


#get students data by path parameters (by id)
@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(description='lets see the data',gt=0)):
    return students[student_id]


#get students data by query parameters (by name)
@app.get('/get_by_name/')
def get_by_name(name: str = None):
    for a in students:
        if students[a]['name'] == name:
            return students[a]
    return {'error' : 'data not found'}

#create new student data
@app.post('/create_student/{student_id}')
def create_student(student_id : int, student: Student):
    if student_id in students:
        return {'Error':'already axisted'}
    students[student_id] = student
    return students[student_id]


#update student data
@app.put('/update_student/{student_id}')
def update_student(student_id: int, student : Update_student):
    if student_id not in students:
        return {'Error':'not valid data'}
    
    if student.name != None:
        students[student_id].name=student.name

    if student.age != None:
        students[student_id].age=student.age
    
    return students[student_id]

@app.delete('/delete_student/{student_id}')
def delete_student(student_id : int):
    if student_id not in students:
        return {'Error':'Student does not exit'}
    
    del students[student_id]

    return {'success':'successfully deleted'}