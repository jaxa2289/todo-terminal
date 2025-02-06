from typing import Optional

from model.file import *
from model.category import *
from model.user import *
from model.todo1 import *
from template.acount_ui import *
# ctrl + space*2


session_user: Optional['User'] = None






class UI:

    def register(self):
        user = {
            "fullname": input("Enter your fullname:"),
            "email": input("Enter your email:"),
            "password": input("Enter your password:")
        }

        user = User(**user)
        user.is_validation()
        user.save()
        self.main()

    def login(self):
        global session_user
        login_data = {
            "email": input("Email:"),
            "password": input("Password:")
        }
        user = User(**login_data)
        session_user = user.is_authentication()
        UIaccount().account()

    def main(self):
        try:
            menu = """
                1) Register
                2) Login
                3) exit
                >>>"""
            key = input(menu)
            match key:
                case "1":
                    self.register()
                case "2":
                    self.login()
                case "3":
                    return
        except AssertionError as message:
            print(message)
            self.main()


