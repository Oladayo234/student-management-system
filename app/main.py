from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import client
from app.routes.user_routes import router as user_router
from app.routes.course_routes import router as course_router
from app.routes.enrollment_routes import router as enrollment_router
from app.exceptions.handlers import register_exception_handlers

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Connected to MongoDB")
    yield
    client.close()
    print("Disconnected from MongoDB")

app = FastAPI(title="Student Course Management System", lifespan=lifespan)

register_exception_handlers(app)

app.include_router(user_router)
app.include_router(course_router)
app.include_router(enrollment_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)