from fastapi import FastAPI
from pydantic import BaseModel
#تعريف البيانات 
class student (BaseModel):
    id:int
    name:str
    grade:float
#تخزين البيانات 
students= [
    student(id=1,name="ahmed",grade=6.5),
    student(id=2,name="salah",grade=10),

]

app=FastAPI()
@app.get("/studentstable")
def studentstable():
    return students


#post method للاضافه
@app.post("/studentstable/add")
def ADDstudent(NEW_STUDENT:student):
    students.append(NEW_STUDENT)
    return{"message":"studentAdded"}

#put method تعديل بيانات
@app.put("/studentstable/{id}")
def update(id:int,updated_student:student):
    for i,student in enumerate(students):
        if student.id==id:
            students[i]=updated_student
            return{"message":"studentApdated","updated_student":updated_student}
    return{"message":"id not found"}


@app.delete("/studentstable")
def delete(id:int):
    for i,student in enumerate(students):
        if student.id==id:  
            del students[i]
            return{"message":"deleted"}
        return{"message":"id not found"}
