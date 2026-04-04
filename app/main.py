from fastapi import FastAPI
from app.database import client
from app.routes.user_routes import router as user_router
from app.routes.course_routes import router as course_router
from app.routes.enrollment_routes import router as enrollment_router
from app.exceptions.handlers import register_exception_handlers

app = FastAPI(title="Student Course Management System")

register_exception_handlers(app)

app.include_router(user_router)
app.include_router(course_router)
app.include_router(enrollment_router)

@app.on_event("startup")
async def startup():
    print("Connected to MongoDB")

@app.on_event("shutdown")
async def shutdown():
    client.close()
    print("Disconnected from MongoDB")