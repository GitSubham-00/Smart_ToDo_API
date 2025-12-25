from fastapi import FastAPI

from app.routes import auth,tasks
app = FastAPI(
    title="Smart ToDo API",
    description="A secure REST API for managing tasks",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Smart ToDo API is running 🚀"}

