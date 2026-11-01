from pydantic import BaseModel

class student_dto(BaseModel):
    full_name: str
    student_id: str
    age: int
    email: str
    course: str