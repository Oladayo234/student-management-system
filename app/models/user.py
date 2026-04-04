from app.models.role import Role

class User:
    def __init__(self, name: str, email: str, role: Role):
        self.__name = name
        self.__email = email
        self.__role = role