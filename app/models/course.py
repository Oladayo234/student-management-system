import code
from datetime import datetime


class Course:
    def __init__(self, title: str, description: str, facilitator_id: str):
        self.__title = title
        self.__description = description
        self.__code = code
        self.__facilitator_id = facilitator_id
        self.__created_at = datetime.now()