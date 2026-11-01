from fastapi import FastAPI

app = FastAPI(
    title="student-data-api",
    version="1.0.0"
)

@app.get("/heart-beat")
def heart_beat():
    return {"message": "API is running!"}
