from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions import (UserNotFoundException, CourseNotFoundException, EnrollmentNotFoundException, DuplicateEnrollmentException, UnauthorizedRoleException,DuplicateEmailException, DuplicateCourseCodeException
)

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(UserNotFoundException)
    async def user_not_found_handler(request: Request, exc: UserNotFoundException):
        return JSONResponse(status_code=404, content={"detail": exc.message})

    @app.exception_handler(CourseNotFoundException)
    async def course_not_found_handler(request: Request, exc: CourseNotFoundException):
        return JSONResponse(status_code=404, content={"detail": exc.message})

    @app.exception_handler(EnrollmentNotFoundException)
    async def enrollment_not_found_handler(request: Request, exc: EnrollmentNotFoundException):
        return JSONResponse(status_code=404, content={"detail": exc.message})

    @app.exception_handler(DuplicateEnrollmentException)
    async def duplicate_enrollment_handler(request: Request, exc: DuplicateEnrollmentException):
        return JSONResponse(status_code=400, content={"detail": exc.message})

    @app.exception_handler(UnauthorizedRoleException)
    async def unauthorized_role_handler(request: Request, exc: UnauthorizedRoleException):
        return JSONResponse(status_code=403, content={"detail": exc.message})

    @app.exception_handler(DuplicateEmailException)
    async def duplicate_email_handler(request: Request, exc: DuplicateEmailException):
        return JSONResponse(status_code=400, content={"detail": exc.message})

    @app.exception_handler(DuplicateCourseCodeException)
    async def duplicate_course_code_handler(request: Request, exc: DuplicateCourseCodeException):
        return JSONResponse(status_code=400, content={"detail": exc.message})