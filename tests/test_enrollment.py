import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio

async def test_enroll_student(client: AsyncClient):
    student = await client.post("/users/", json={
        "name": "Enrolled Student",
        "email": "enrolled@semicolon.africa",
        "role": "student"
    })
    student_id = student.json()["id"]

    facilitator = await client.post("/users/", json={
        "name": "Course Facilitator",
        "email": "coursefacilitator@semicolon.africa",
        "role": "facilitator"
    })
    facilitator_id = facilitator.json()["id"]

    course = await client.post("/courses/", json={
        "title": "Test Course",
        "description": "Test Description",
        "facilitator_id": facilitator_id
    })
    course_id = course.json()["id"]

    response = await client.post("/enrollments/", json={
        "student_id": student_id,
        "course_id": course_id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_id
    assert data["course_id"] == course_id
    assert data["grade"] is None

async def test_duplicate_enrollment(client: AsyncClient):
    student = await client.post("/users/", json={
        "name": "Dup Student",
        "email": "dupstudent@semicolon.africa",
        "role": "student"
    })
    student_id = student.json()["id"]

    facilitator = await client.post("/users/", json={
        "name": "Dup Facilitator",
        "email": "dupfacilitator@semicolon.africa",
        "role": "facilitator"
    })
    facilitator_id = facilitator.json()["id"]

    course = await client.post("/courses/", json={
        "title": "Dup Course",
        "description": "Dup Description",
        "facilitator_id": facilitator_id
    })
    course_id = course.json()["id"]

    await client.post("/enrollments/", json={
        "student_id": student_id,
        "course_id": course_id
    })
    response = await client.post("/enrollments/", json={
        "student_id": student_id,
        "course_id": course_id
    })
    assert response.status_code == 400

async def test_assign_grade(client: AsyncClient):
    student = await client.post("/users/", json={
        "name": "Grade Student",
        "email": "gradestudent@semicolon.africa",
        "role": "student"
    })
    student_id = student.json()["id"]

    facilitator = await client.post("/users/", json={
        "name": "Grade Facilitator",
        "email": "gradefacilitator@semicolon.africa",
        "role": "facilitator"
    })
    facilitator_id = facilitator.json()["id"]

    course = await client.post("/courses/", json={
        "title": "Grade Course",
        "description": "Grade Description",
        "facilitator_id": facilitator_id
    })
    course_id = course.json()["id"]

    enrollment = await client.post("/enrollments/", json={
        "student_id": student_id,
        "course_id": course_id
    })
    enrollment_id = enrollment.json()["id"]

    response = await client.patch(f"/enrollments/{enrollment_id}/grade", json={
        "grade": "A"
    })
    assert response.status_code == 200