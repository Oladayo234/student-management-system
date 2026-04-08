from app.models.role import Role
from app.models.user import User


class Admin(User):
    def __init__(self, name: str, email: str):
        super().__init__(name, email, Role.ADMIN)