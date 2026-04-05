from app.models.user import User
from app.models.role import Role

class Facilitator(User):
    def __init__(self, name: str, email: str):
        super().__init__(name, email, Role.FACILITATOR)