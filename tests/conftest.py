import pytest
import mongomock
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch
from app.main import app
import app.database as database

@pytest.fixture(scope="session", autouse=True)
def mock_db():
    mock_client = mongomock.MongoClient()
    mock_database = mock_client["student_course_db"]
    with patch("app.database.db", mock_database):
        yield mock_database

@pytest.fixture(scope="session")
async def client(mock_db):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c