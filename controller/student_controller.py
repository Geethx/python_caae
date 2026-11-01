from fastapi import APIRouter
from model.student import student_dto as Student

router = APIRouter(prefix="/student", tags=["Student"])

@router.post("")
def save_student(student: Student):
    print(f"Student is: {student}")
    return {
        "message": "Student data saved successfully!", 
        "student": student
    }