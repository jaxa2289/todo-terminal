
from colorama import Fore
from tabulate import tabulate
from template.category_ui import *
from template.todo_ui import *
from typing import Optional

class UIaccount:
    session_user: Optional['User'] = None
    def panel(self):

        menu = """
            1) Category
            2) ToDo
            0) <-back
            >>>"""
        key = input(menu)

        match key:
            case "1":

                UICategory().main()
            case "2":
                UITodo().main()
            case "0":
                self.account()

    def account(self):
        from template.ui import session_user
        self.session_user = session_user
        print(f"Welcome to account {self.session_user.fullname}")
        from template.ui import UI
        menu = [
            ['1', 'Panel'],
            ['2 ','Settings'],
            ['0', '<-back']
        ]
        print(Fore.CYAN + tabulate(menu, tablefmt="fancy_grid"))
        try:
            key = input('>>>')
            assert key in ('1', '2', '0'), "Invalid option!"
            match key:
                case "1":
                    self.panel()
                case "2":
                    self.settings()
                case "0":
                    UI().main()
        except AssertionError as message:
            print(Fore.RED + str(message))
            self.account()

    def edit(self):
        try:
            fields = [
                ['1 ', 'Full name'],
                ['2 ', 'Email'],
                ['3 ', 'Password'],
                ['0 ', '<-back']
            ]
            print(Fore.LIGHTMAGENTA_EX + tabulate(fields, tablefmt="grid"))
            field = input(">>>>")
            if field == "0":
                self.settings()
                return

            new_val = input("New value")
            match field:
                case "1":
                    self.session_user =self.session_user.update("fullname", new_val)
                    self.edit()
                case "2":
                    temp_user = User(email=new_val)
                    temp_user.is_validation2("email")
                    self.session_user =self.session_user.update("email", new_val)
                    self.edit()
                case "3":
                    temp_user = User(password=new_val)
                    temp_user.is_validation2("password")
                    self.session_user =self.session_user.update("password", new_val)
                    self.edit()

        except AssertionError as error:
            print(Fore.RED + str(error))
            self.edit()

    def settings(self):

        menu = """
                1) Edit account
                2) About
                3) delete account
                0) <-back
                >>>"""
        key = input(menu)
        match key:

            case "1":
                self.edit()
            case "2":
                print(self.session_user.about())
                self.settings()
            case "3":
                from template.ui import UI
                self.session_user.delete()
                UI().main()
            case "0":
                self.account()