import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio

async def test_create_course(client: AsyncClient):
    facilitator = await client.post("/users/", json={
        "name": "Test Facilitator",
        "email": "facilitator@semicolon.africa",
        "role": "facilitator"
    })
    facilitator_id = facilitator.json()["id"]

    response = await client.post("/courses/", json={
        "title": "Python Backend",
        "description": "Learn FastAPI and MongoDB",
        "facilitator_id": facilitator_id
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Python Backend"
    assert data["facilitator_id"] == facilitator_id

async def test_create_course_invalid_facilitator(client: AsyncClient):
    response = await client.post("/courses/", json={
        "title": "Python Backend",
        "description": "Learn FastAPI",
        "facilitator_id": "000000000000000000000000"
    })
    assert response.status_code == 404

async def test_student_cannot_create_course(client: AsyncClient):
    student = await client.post("/users/", json={
        "name": "Test Student",
        "email": "student_course@semicolon.africa",
        "role": "student"
    })
    student_id = student.json()["id"]

    response = await client.post("/courses/", json={
        "title": "Python Backend",
        "description": "Learn FastAPI",
        "facilitator_id": student_id
    })
    assert response.status_code == 403

async def test_get_all_courses(client: AsyncClient):
    response = await client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)