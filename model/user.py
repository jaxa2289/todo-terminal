from dataclasses import dataclass

from typing import Optional
from model.file import *



@dataclass
class User(File):
    id :Optional[int] = None
    fullname:Optional[str] = None
    email:Optional[str] = None
    password:Optional[str] = None

    def is_validation(self):
        users: list[User] = self.get()
        for user in users:
            assert self.email and user.email != self.email, "Bunday email mavjut!!"
        assert self.password and  len(self.password) >= 4 , "Password Qisqa!!"
        assert self.email and self.email.endswith("@gmail.com"), "Invalid email"

    def is_validation2(self, turi: str):
        users: list[User] = self.get()

        if turi == "email":

            for user in users:
                if user.email == self.email:
                    raise AssertionError("Bunday email mavjud!!")
            assert self.email and self.email.endswith("@gmail.com"), "Invalid email!"

        if turi == "password":
            assert self.password and len(self.password) >= 4, "Password qisqa!"

    def is_authentication(self)->'User':
        users:list['User'] = self.get()
        for user in users:
            if user.email == self.email:
                assert user.password == self.password , "Password Error"
                return user
        raise AssertionError(" account error")

    def about(self):

        text = f"""
            id : {self.id}
            fullname : {self.fullname}
            email : {self.email}
            password : {self.password}
                """
        return text












