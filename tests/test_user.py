import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio

async def test_create_student(client: AsyncClient):
    response = await client.post("/users/", json={
        "name": "Dayo Adeyemi",
        "email": "dayo@semicolon.africa",
        "role": "student"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Dayo Adeyemi"
    assert data["email"] == "dayo@semicolon.africa"
    assert data["role"] == "student"
    assert "id" in data

async def test_create_facilitator(client: AsyncClient):
    response = await client.post("/users/", json={
        "name": "John Facilitator",
        "email": "john@semicolon.africa",
        "role": "facilitator"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["role"] == "facilitator"

async def test_create_user_duplicate_email(client: AsyncClient):
    await client.post("/users/", json={
        "name": "Dayo Adeyemi",
        "email": "duplicate@semicolon.africa",
        "role": "student"
    })
    response = await client.post("/users/", json={
        "name": "Another User",
        "email": "duplicate@semicolon.africa",
        "role": "student"
    })
    assert response.status_code == 400

async def test_get_user(client: AsyncClient):
    create_response = await client.post("/users/", json={
        "name": "Test User",
        "email": "testuser@semicolon.africa",
        "role": "student"
    })
    user_id = create_response.json()["id"]
    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id

async def test_get_user_not_found(client: AsyncClient):
    response = await client.get("/users/000000000000000000000000")
    assert response.status_code == 404