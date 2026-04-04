class UnauthorizedRoleException(Exception):
    def __init__(self, message="Unauthorized role"):
        self.message = message
        super().__init__(self.message)