from fastapi import FastAPI
from controller.student_controller import router as student_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="student-data-api",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(student_router)

@app.get("/heart-beat")
def heart_beat():
    return {"message": "API is running!"}
