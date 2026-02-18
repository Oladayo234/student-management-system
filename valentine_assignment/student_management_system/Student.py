import re
class Student:
    __id_counter = 1
    def __init__(self, name: str, age: int, gender: str, email: str, phone_number: str):
        self.__student_id = Student.__id_counter
        Student.__id_counter += 1

        self.set_name(name)
        self.set_age(age)
        self.set_gender(gender)
        self.set_email(email)
        self.set_phone_number(phone_number)

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def set_name(self, name:str):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = name.strip()

    def set_age(self, age:int):
        if 16 <= age <= 60:
            self.__age = age
        else:
            raise ValueError("Invalid age")

    def set_gender(self, gender:str):
        gender = gender.lower()
        if gender not in ("male", "female"):
            raise ValueError("Invalid gender")
        else:
            self.__gender = gender

    def set_email(self, email:str):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            self.__email = email
        else:
            raise ValueError("Invalid email format")

    def set_phone_number(self, phone_number:str):
        if not phone_number.isdigit():
            raise ValueError("Phone number must contain digits only")
        if len(phone_number) != 11:
            raise ValueError("Invalid phone number")
        else:
            self.__phone_number = phone_number

    def __str__(self):
        return (f"Student ID: {self.__student_id}, "
                f"Name: {self.__name}, "
                f"Age: {self.__age}, "
                f"Gender: {self.__gender}, "
                f"Email: {self.__email}, "
                f"Phone: {self.__phone_number}")


