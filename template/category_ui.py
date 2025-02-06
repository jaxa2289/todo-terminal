from typing import Optional

from model.file import *
from model.category import *
from model.user import *
from model.todo1 import *


class UICategory:
    session_category : Optional['Category'] = None
    def main(self):
        from template.acount_ui import UIaccount
        menu = """
            *) Search 🔍
            1) Add
            2) List
            0) <-back
        >>>"""
        key = input(menu)
        assert key in ("*", "1", "2", "0"), "Menuyada yo'q bo'lim tanlandi"

        match key:
            case "*":
                short_name = input("🔍>>>")
                find_categories = Category().search(short_name)
                for i, category in enumerate(find_categories,1):
                    print(f"{i}) {category.name}")
                print("0) <-back")
                pos = input(">>>")
                if pos == "0":
                    self.main()
                    return
                self.session_category = find_categories[int(pos)-1]
                self.settings()


            case "1":
                _name = input("Name:")
                Category(name=_name).save()
                self.main()

            case "2":
                categories = Category().get()
                for i, category in enumerate(categories, 1):
                    print(f"{i}) {category.name}")
                print("0) <-back")
                pos = input(">>>")
                if pos == "0":
                    self.main()
                    return
                self.session_category = categories[int(pos) - 1]
                self.settings()
            case "0":
                UIaccount().panel()

    def settings(self):
        menu = """
            1) delete
            2) update
            3) about
            0) <-back
            >>>"""
        match input(menu):
            case "1":
                self.session_category.delete()
                self.main()
            case "2":
                fields = """
                    1) name
                    0) <-back
                >>>"""
                key = input(fields)
                if key == "0":
                    self.settings()
                    return
                new_value = input("New value:")
                match key:
                    case "1":
                        self.session_category =self.session_category.update("name" , new_value)
                        self.settings()

            case "3":
                print(self.session_category.about())
                self.settings()
            case "0":
                self.main()